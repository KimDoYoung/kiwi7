// kiwoom-base.improved.js
// 의존성 주입 + 추가 개선사항 적용
window.createKiwoomBase = function createKiwoomBase(config, depends = {}) {
  // 설정 검증
  if (!config) throw new Error('config는 필수입니다');
  if (!config.table?.columns?.length) throw new Error('config.table.columns가 필요합니다');
  if (!config.api_endpoint) throw new Error('config.api_endpoint가 필요합니다');

  const {
    callApi = (ep, payload) => { throw new Error('deps.callApi가 필요합니다'); },
    utils = { 
      autoRefreshManager: { start(){}, stop(){}, stopAll(){} }, 
      exportToCSV(){} 
    },
    debug = false,
  } = depends;

  // 내부 상태 (클로저로 캡슐화)
  let data_version = 0;
  let cache_key = null;
  let cached_items = [];
  let auto_refresh_key = null;

  // 상수 정의
  const CONSTANTS = {
    DEFAULT_EMPTY_VALUE: '-',
    PROFIT_COLORS: {
      POSITIVE: 'text-danger',
      NEGATIVE: 'text-primary'
    },
    TEXT_ALIGN_PREFIX: 'text-'
  };

  // 로깅 유틸리티
  const logger = {
    log: (...args) => debug && console.log('[KiwoomBase]', ...args),
    warn: (...args) => console.warn('[KiwoomBase]', ...args),
    error: (...args) => console.error('[KiwoomBase]', ...args)
  };

  // 데이터 유틸리티
  const dataUtils = {
    findArrayInData(data, dataKey) {
      if (!data) return null;
      if (dataKey && Array.isArray(data?.[dataKey])) return data[dataKey];
      
      for (const [key, value] of Object.entries(data)) {
        if (Array.isArray(value) && value.length) {
          logger.log(`Found array at key: ${key} with ${value.length} items`);
          return value;
        }
      }
      return null;
    },

    toNumber(value, fallback = NaN) {
      if (typeof value === 'number') return value;
      if (typeof value === 'string') {
        const cleaned = value.replace(/[^\d.-]/g, '');
        const num = parseFloat(cleaned);
        return Number.isFinite(num) ? num : fallback;
      }
      const num = Number(value);
      return Number.isFinite(num) ? num : fallback;
    },

    isEmpty(value) {
      return value === null || value === undefined || value === '';
    }
  };

  // 포맷터
  const formatters = {
    number: (value) => {
      const num = dataUtils.toNumber(value);
      return Number.isFinite(num) ? num.toLocaleString() : CONSTANTS.DEFAULT_EMPTY_VALUE;
    },

    percent: (value) => {
      const num = dataUtils.toNumber(value);
      return Number.isFinite(num) ? num.toFixed(2) + '%' : CONSTANTS.DEFAULT_EMPTY_VALUE;
    },

    currency: (value) => {
      const num = dataUtils.toNumber(value);
      return Number.isFinite(num) ? num.toLocaleString() + '원' : CONSTANTS.DEFAULT_EMPTY_VALUE;
    },

    profit: (value) => {
      const num = dataUtils.toNumber(value);
      return Number.isFinite(num) ? num.toLocaleString() : CONSTANTS.DEFAULT_EMPTY_VALUE;
    },

    default: (value) => {
      return dataUtils.isEmpty(value) ? CONSTANTS.DEFAULT_EMPTY_VALUE : String(value);
    }
  };

  // 스타일 유틸리티
  const styleUtils = {
    getProfitClass(value) {
      const num = dataUtils.toNumber(value);
      if (!Number.isFinite(num)) return '';
      if (num > 0) return CONSTANTS.PROFIT_COLORS.POSITIVE;
      if (num < 0) return CONSTANTS.PROFIT_COLORS.NEGATIVE;
      return '';
    },

    getAlignClass(align) {
      return align ? CONSTANTS.TEXT_ALIGN_PREFIX + align : '';
    }
  };

  // 캐시 관리
  const cacheManager = {
    clearCache() {
      cache_key = null;
      cached_items = [];
    },

    generateKey(sortKey, sortAsc, filterCount) {
      return `${sortKey}|${sortAsc ? 'asc' : 'desc'}|${filterCount}|v${data_version}`;
    },

    isValid(key) {
      return cache_key === key && Array.isArray(cached_items);
    },

    set(key, items) {
      cache_key = key;
      cached_items = items;
    }
  };

  // 기본 정렬 키 결정
  const getDefaultSortKey = () => {
    const columns = config.table?.columns || [];
    const sortableColumn = columns.find(c => c.sortable);
    return sortableColumn?.key || columns[0]?.key;
  };

  // 값 추출 (파생 컬럼 지원)
  const extractValue = (item, column) => {
    if (typeof column.formula === 'function') {
      try {
        return column.formula(item);
      } catch (error) {
        logger.error('Formula execution error:', error);
        return null;
      }
    }
    
    if (typeof column.selector === 'function') {
      try {
        return column.selector(item);
      } catch (error) {
        logger.error('Selector execution error:', error);
        return null;
      }
    }
    
    return item?.[column.key];
  };

  // 정렬 함수
  const createSorter = (column, isAscending) => {
    return (a, b) => {
      if (typeof column.sorter === 'function') {
        try {
          return column.sorter(a, b, { 
            asc: isAscending, 
            selector: (item) => extractValue(item, column) 
          });
        } catch (error) {
          logger.error('Custom sorter error:', error);
          return 0;
        }
      }

      const aValue = extractValue(a, column);
      const bValue = extractValue(b, column);
      
      const aNum = dataUtils.toNumber(aValue);
      const bNum = dataUtils.toNumber(bValue);
      
      let comparison;
      if (Number.isFinite(aNum) && Number.isFinite(bNum)) {
        comparison = aNum - bNum;
      } else {
        const aStr = String(aValue ?? '');
        const bStr = String(bValue ?? '');
        comparison = aStr.localeCompare(bStr);
      }
      
      return isAscending ? comparison : -comparison;
    };
  };

  // 자동 새로고침 관리
  const autoRefreshManager = {
    start() {
      if (!config.auto_refresh) return;
      
      const key = `${config.api_endpoint}::${config.title || Date.now()}`;
      auto_refresh_key = key;
      
      utils.autoRefreshManager.start(
        key,
        () => instance.fetch_data(),
        config.auto_refresh
      );
      
      logger.log('Auto refresh started:', key);
    },

    stop() {
      if (auto_refresh_key) {
        utils.autoRefreshManager.stop?.(auto_refresh_key);
        logger.log('Auto refresh stopped:', auto_refresh_key);
        auto_refresh_key = null;
      }
    },

    toggle() {
      if (auto_refresh_key) {
        this.stop();
      } else {
        this.start();
      }
    }
  };

  // 메인 인스턴스
  const instance = {
    // ---- 상태 ----
    data: null,
    return_code: 0,
    return_msg: null,
    loading: false,
    sort_key: getDefaultSortKey(),
    sort_asc: true,
    
    // 핸들러들
    filter_functions: [],
    callbacks: [],
    handlers: { cell: {} },
    
    debug,

    // ---- 생명주기 ----
    init() {
      this.fetch_data();
      autoRefreshManager.start();
      this._setupCleanup();
    },

    destroy() {
      autoRefreshManager.stop();
    },

    _setupCleanup() {
      // Alpine.js의 생명주기나 컴포넌트 파괴 시점에 맞춰 정리
      const cleanup = () => this.destroy();
      
      if (typeof window !== 'undefined') {
        window.addEventListener('beforeunload', cleanup);
      }
      
      // Alpine.js의 $cleanup 훅이 있다면 사용
      if (typeof this.$cleanup === 'function') {
        this.$cleanup(cleanup);
      }
    },

    // ---- 필터 관리 ----
    addFilter(filterFunction) {
      if (typeof filterFunction !== 'function') {
        logger.error('addFilter expects a function');
        return false;
      }
      
      this.filter_functions.push(filterFunction);
      cacheManager.clearCache();
      logger.log(`Filter added. Total: ${this.filter_functions.length}`);
      return true;
    },

    clearFilters() {
      this.filter_functions = [];
      cacheManager.clearCache();
      logger.log('All filters cleared');
    },

    activeFilterCount() {
      return this.filter_functions.length;
    },

    // ---- 콜백 관리 ----
    addCallback(callbackFunction) {
      if (typeof callbackFunction !== 'function') {
        logger.error('addCallback expects a function');
        return false;
      }
      
      this.callbacks.push(callbackFunction);
      logger.log(`Callback added. Total: ${this.callbacks.length}`);
      return true;
    },

    clearCallbacks() {
      this.callbacks = [];
      logger.log('All callbacks cleared');
    },

    // ---- 셀 클릭 핸들러 ----
    addClickHandler(columnKey, handler) {
      if (typeof handler !== 'function') {
        logger.error(`addClickHandler expects a function for column: ${columnKey}`);
        return false;
      }
      
      this.handlers.cell[columnKey] = handler;
      logger.log(`Click handler added for: ${columnKey}`);
      return true;
    },

    clearClickHandlers() {
      this.handlers.cell = {};
      logger.log('All click handlers cleared');
    },

    handleCellClick(item, column) {
      if (!column.clickable) return;
      
      logger.log('Cell clicked:', column.key);
      
      const handler = this.handlers.cell[column.key] || this._defaultCellClick;
      try {
        handler.call(this, item, column, this);
      } catch (error) {
        logger.error(`Cell click handler error for ${column.key}:`, error);
      }
    },

    _defaultCellClick(item, column) {
      const defaultHandlers = {
        '종목코드': (item) => {
          const code = String(item[column.key] || '').match(/\d{6}/)?.[0];
          if (code) {
            window.open(`https://finance.naver.com/item/main.naver?code=${code}`, '_blank');
          }
        },
        '종목명': (item) => {
          alert(`종목명: ${item[column.key]}`);
        }
      };

      const handler = defaultHandlers[column.key];
      if (handler) {
        handler(item);
      } else {
        logger.log('Default cell click:', column.key, item[column.key]);
      }
    },

    // ---- 정렬 ----
    sortBy(key) {
      if (this.sort_key === key) {
        this.sort_asc = !this.sort_asc;
      } else {
        this.sort_key = key;
        this.sort_asc = true;
      }
      cacheManager.clearCache();
    },

    // ---- 포맷팅 ----
    formatValue(value, format) {
      if (dataUtils.isEmpty(value)) return CONSTANTS.DEFAULT_EMPTY_VALUE;
      
      const formatter = formatters[format] || formatters.default;
      try {
        return formatter(value);
      } catch (error) {
        logger.error('Format error:', error);
        return formatters.default(value);
      }
    },

    getTableColumns() {
      return Array.isArray(config.table?.columns) ? config.table.columns : [];
    },

    getSummaryValue(field) {
      const value = this.data?.[field.key];
      return this.formatValue(value, field.format || 'currency');
    },

    getCellValue(item, column) {
      const value = extractValue(item, column);
      return this.formatValue(value, column.format);
    },

    getCellClass(item, column) {
      const classes = [];
      
      // 정렬 클래스
      const alignClass = styleUtils.getAlignClass(column.align);
      if (alignClass) classes.push(alignClass);
      
      // 손익 색상 클래스
      const shouldApplyProfitColor = column.profit_loss || 
                                   column.format === 'profit' || 
                                   column.key === '주당손익';
      
      if (shouldApplyProfitColor) {
        const value = extractValue(item, column);
        const profitClass = styleUtils.getProfitClass(value);
        if (profitClass) classes.push(profitClass);
      }
      
      return classes.join(' ');
    },

    // ---- 데이터 접근 ----
    totalItemCount() {
      const items = dataUtils.findArrayInData(this.data, config.table?.data_key);
      return Array.isArray(items) ? items.length : 0;
    },

    filteredItemCount() {
      const items = dataUtils.findArrayInData(this.data, config.table?.data_key);
      if (!Array.isArray(items)) return 0;
      if (!this.filter_functions.length) return items.length;
      
      return items.filter(row => 
        this.filter_functions.every(filterFunc => {
          try {
            return filterFunc(row);
          } catch (error) {
            logger.error('Filter function error:', error);
            return true; // 에러 시 포함
          }
        })
      ).length;
    },

    // ---- 메인 데이터 getter (캐시 적용) ----
    sortedItems() {
      if (!this.data || this.loading) return [];

      const cacheKey = cacheManager.generateKey(
        this.sort_key, 
        this.sort_asc, 
        this.filter_functions.length
      );

      if (cacheManager.isValid(cacheKey)) {
        logger.log('Returning cached items');
        return cached_items;
      }

      logger.log('Computing sorted items...');
      
      // 1. 원본 데이터 가져오기
      const items = dataUtils.findArrayInData(this.data, config.table?.data_key) || [];
      
      // 2. 필터 적용
      const filteredItems = this.filter_functions.length === 0 
        ? items 
        : items.filter(row => 
            this.filter_functions.every(filterFunc => {
              try {
                return filterFunc(row);
              } catch (error) {
                logger.error('Filter error:', error);
                return true;
              }
            })
          );
      
      // 3. 정렬 적용
      const sortColumn = this.getTableColumns().find(c => c.key === this.sort_key) || 
                        { key: this.sort_key };
      
      const sorter = createSorter(sortColumn, this.sort_asc);
      const sortedItems = [...filteredItems].sort(sorter);
      
      // 4. 캐시 저장
      cacheManager.set(cacheKey, sortedItems);
      
      logger.log(`Computed ${sortedItems.length} sorted items from ${items.length} total`);
      return sortedItems;
    },

    // ---- API 호출 ----
    async fetch_data(
        endpoint = config.api_endpoint,
        payload = config.payload || {}  
    ) {
      this.loading = true;
      
      try {
        logger.log('Fetching data...', endpoint);
        
        // const response = await callApi(config.api_endpoint, config.payload);
        const response = await callApi(endpoint, payload);
        
        if (!response?.success) {
          throw new Error(response?.error_message || 'API 호출 실패');
        }

        this.data = response.data;
        this.return_code = response.data?.return_code ?? 0;
        this.return_msg = response.data?.return_msg ?? config.api_endpoint + ' 조회 성공';
        
        data_version++;
        cacheManager.clearCache();
        
        logger.log('Data fetched successfully');

        // 콜백 실행
        await this._executeCallbacks();
        
        // DOM 업데이트 알림
        this._notifyDataUpdate();
        
      } catch (error) {
        this.return_code = -1;
        this.return_msg = '오류: ' + (error?.message || error);
        logger.error('API 호출 오류:', error);
      } finally {
        this.loading = false;
      }
    },

    async _executeCallbacks() {
      if (this.callbacks.length === 0) return;
      
      logger.log(`Executing ${this.callbacks.length} callbacks...`);
      
      for (const callback of this.callbacks) {
        try {
          await callback(this.data, this);
        } catch (error) {
          logger.error('Callback execution error:', error);
        }
      }
      
      logger.log('All callbacks executed');
    },

    _notifyDataUpdate() {
      const notify = () => {
        if (typeof this.$dispatch === 'function') {
          this.$dispatch('data-updated');
        }
      };

      if (typeof this.$nextTick === 'function') {
        this.$nextTick(notify);
      } else {
        queueMicrotask(notify);
      }
    },

    // ---- 유틸리티 메서드 ----
    exportCSV() {
      const filename = `${config.title || 'data'}_${new Date().toISOString().slice(0, 10)}.csv`;
      
      if (utils.exportToCSV) {
        utils.exportToCSV(this.sortedItems(), this.getTableColumns(), filename);
      } else {
        logger.error('exportToCSV utility not available');
      }
    },

    refresh() {
      this.fetch_data();
    },

    toggleAutoRefresh() {
      autoRefreshManager.toggle();
    },

    // ---- 액션 버튼 ----
    hasActionButtons() {
      return config.action_buttons && config.action_buttons.length > 0;
    },

    getActions() {
      return config.action_buttons || [];
    }
  };

  return instance;
};
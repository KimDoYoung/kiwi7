// kiwoom-base.js 수정
window.KiwoomBase = function(config) {
    if (!config) {
        throw new Error(`api에 따른 설정값을 인자가 필요합니다. `);
    }

    return {
        data: null,
        return_code: 0,
        return_msg: null,
        loading: false,
        sort_key: config.table.columns.find(col => col.sortable)?.key || config.table.columns[0].key,
        sort_asc: true,
        
        // 캐시 관련
        _cached_items: null,
        _cache_key: '',        
        
        // 필터 관련
        filter_functions: [],
        
        // 콜백 관련
        callbacks: [],

        // cell 클릭 함수들
        clickHandlers: {},

        config,  // 설정 객체 보관

        init() {
            this.fetch_data();

            if (config.auto_refresh) {
                window.KiwoomUtils.autoRefreshManager.start(
                    config.api_endpoint,
                    () => this.fetch_data(),
                    config.auto_refresh
                );
            }

            window.addEventListener('beforeunload', () => {
                window.KiwoomUtils.autoRefreshManager.stopAll();
            });
        },

        async _get_data_hash() {
            if (!this.data) return 0;
            
            const dataString = JSON.stringify(this.data);
            const encoder = new TextEncoder();
            const data = encoder.encode(dataString);
            const hashBuffer = await crypto.subtle.digest('SHA-256', data);
            
            const hashArray = new Uint32Array(hashBuffer.slice(0, 8));
            return hashArray[0] ^ hashArray[1];
        },

        // ⭐ formatValue 메서드 추가
        formatValue(value, format) {
            if (value === null || value === undefined || value === '') {
                return '-';
            }

            const numValue = parseFloat(value);
            if (isNaN(numValue)) {
                return value;
            }

            switch (format) {
                case 'number':
                    return numValue.toLocaleString();
                case 'percent':
                    return numValue.toFixed(2) + '%';
                case 'profit':
                    const formattedValue = numValue.toLocaleString();
                    return formattedValue;
                case 'currency':
                    return numValue.toLocaleString() + '원';
                default:
                    return value;
            }
        },

        // 정렬
        sortBy(key) {
            if (this.sort_key === key) {
                this.sort_asc = !this.sort_asc;
            } else {
                this.sort_key = key;
                this.sort_asc = true;
            }
            this.clearCache();
        },

        // 필터 함수 추가
        addFilter(filterFunc) {
            if (typeof filterFunc === 'function') {
                this.filter_functions.push(filterFunc);
                console.log(`🔍 Filter function added. Total filters: ${this.filter_functions.length}`);
            } else {
                console.error('❌ addFilter expects a function');
            }
        },

        // 모든 필터 초기화
        clearFilters() {
            this.filter_functions = [];
            console.log('✅ All filter functions cleared');
        },

        // 캐시 clear
        clearCache(){
            this._cache_key = undefined;
            this._cached_items = undefined;
        },

        // 콜백 함수 추가
        addCallback(callbackFunc) {
            if (typeof callbackFunc === 'function') {
                this.callbacks.push(callbackFunc);
                console.log(`✅ Callback function added. Total callbacks: ${this.callbacks.length}`);
            } else {
                console.error('❌ addCallback expects a function');
            }
        },

        // 모든 콜백 초기화
        clearCallbacks() {
            this.callbacks = [];
            console.log('✅ All callback functions cleared');
        },

        // ⭐ 클릭 핸들러 등록
        addClickHandler(columnKey, handler) {
            if (typeof handler === 'function') {
                this.clickHandlers[columnKey] = handler;
                console.log(`✅ Click handler added for column: ${columnKey}`);
            } else {
                console.error(`❌ addClickHandler expects a function for column: ${columnKey}`);
            }
        },

        // ⭐ 모든 클릭 핸들러 초기화
        clearClickHandlers() {
            this.clickHandlers = {};
            console.log('✅ All click handlers cleared');
        },
        // ⭐ 셀 클릭 핸들러 (개선됨)
        handleCellClick(item, column) {
            if (!column.clickable) return;

            console.log(`셀 click : ${column.key}`, item);

            // 등록된 커스텀 핸들러가 있는지 확인
            if (this.clickHandlers[column.key]) {
                try {
                    console.log("등록된 cell 클릭...")
                    this.clickHandlers[column.key](item, column, this);
                } catch (error) {
                    console.error(`❌ Click handler error for ${column.key}:`, error);
                }
                return;
            }

            // 기본 핸들러 (커스텀 핸들러가 없을 때)
            this.defaultCellClickHandler(item, column);
        },

        // ⭐ 기본 클릭 핸들러
        defaultCellClickHandler(item, column) {
            switch (column.key) {
                case '종목코드':
                    console.log('기본 종목코드 클릭:', item[column.key]);
                    const stk_code = (item[column.key] || '').match(/\d{6}/)?.[0] || '';
                    window.open(`https://finance.naver.com/item/main.naver?code=${stk_code}`, '_blank');
                    break;
                    
                case '종목명':
                    console.log('기본 종목명 클릭:', item[column.key]);
                    // 기본 동작: 알림
                    alert(`종목명: ${item[column.key]}`);
                    break;
                    
                default:
                    console.log('기본 셀 클릭:', column.key, item[column.key]);
            }
        },


        // 활성 필터 개수
        get activeFilterCount() {
            return this.filter_functions.length;
        },

        // 데이터에서 배열 찾기
        findArrayInData() {
            if (!this.data) return null;

            const dataKey = config.table.data_key;
            if (this.data[dataKey] && Array.isArray(this.data[dataKey])) {
                return this.data[dataKey];
            }

            for (const [key, value] of Object.entries(this.data)) {
                if (Array.isArray(value) && value.length > 0) {
                    console.log(`🔍 Found array at key: ${key} with ${value.length} items`);
                    return value;
                }
            }

            return null;
        },

        // Alpine.js용 캐시된 정렬 아이템 (getter)
        getSortedCachedItems() {
            if (!this.data || this.loading) {
                console.log('❌ No data or loading, returning empty array');
                return [];
            }
            
            const dataHash = this._get_data_hash();
            const currentCacheKey = `${this.sort_key}-${this.sort_asc}-${this.filter_functions.length}-${dataHash}`;
            
            if (this._cache_key !== currentCacheKey) {
                console.log('🔄 sorted_items 캐시 갱신 중...', currentCacheKey);
                this._cached_items = this.getSortedItems();
                this._cache_key = currentCacheKey;
            } else {
                console.log('📋 sorted_items 캐시에서 반환');
            }
            
            return this._cached_items || [];
        },        

        // 필터링 + 정렬된 아이템 가져오기
        getSortedItems() {
            if (this.loading || !this.data) {
                console.log('❌ No data or loading, returning empty array');
                return [];
            }

            let items = this.data?.[config.table.data_key];

            if (!items || !Array.isArray(items)) {
                console.warn('⚠️ Configured key not found, searching for arrays...');
                items = this.findArrayInData();
            }

            if (!items || !Array.isArray(items)) {
                return [];
            }

            // 1. 필터링 먼저 적용
            let filteredItems = items;
            if (this.filter_functions.length > 0) {
                filteredItems = items.filter(item => {
                    return this.filter_functions.every(filterFunc => {
                        try {
                            return filterFunc(item);
                        } catch (error) {
                            console.error('❌ Filter function error:', error);
                            return true;
                        }
                    });
                });
                console.log(`🔍 Filtered ${items.length} → ${filteredItems.length} items using ${this.filter_functions.length} filter(s)`);
            }

            // 2. 정렬 적용 (파생 컬럼 지원)
            const sortedItems = [...filteredItems].sort((a, b) => {
                const column = this.config.table.columns.find(col => col.key === this.sort_key);
                let aValue, bValue;

                if (column && column.derived && column.formula) {
                    // 파생 컬럼인 경우
                    aValue = column.formula(a);
                    bValue = column.formula(b);
                } else {
                    // 일반 컬럼인 경우
                    aValue = a[this.sort_key];
                    bValue = b[this.sort_key];
                }

                // 숫자 형태로 변환 시도
                const aNum = parseFloat(aValue);
                const bNum = parseFloat(bValue);
                
                if (!isNaN(aNum) && !isNaN(bNum)) {
                    return this.sort_asc ? aNum - bNum : bNum - aNum;
                }
                
                // 문자열 비교
                const aStr = String(aValue || '');
                const bStr = String(bValue || '');
                return this.sort_asc ? aStr.localeCompare(bStr) : bStr.localeCompare(aStr);
            });
            
            console.log(`✅ Returning ${sortedItems.length} items (${this.filter_functions.length} filters applied, sorted: ${this.sort_key})`);
            
            return sortedItems;
        },

        // 필터링된 총 개수
        filteredItemCount() {
            if (this.loading || !this.data) return 0;
            
            let items = this.data?.[config.table.data_key];
            if (!items || !Array.isArray(items)) {
                items = this.findArrayInData();
            }
            if (!items || !Array.isArray(items)) return 0;

            if (this.filter_functions.length > 0) {
                return items.filter(item => {
                    return this.filter_functions.every(filterFunc => {
                        try {
                            return filterFunc(item);
                        } catch (error) {
                            console.error('❌ Filter function error:', error);
                            return true;
                        }
                    });
                }).length;
            }
            return items.length;
        },

        // 전체 아이템 개수
        totalItemCount() {
            if (this.loading || !this.data) return 0;
            
            let items = this.data?.[config.table.data_key];
            if (!items || !Array.isArray(items)) {
                items = this.findArrayInData();
            }
            if (!items || !Array.isArray(items)) return 0;
            
            return items.length;
        },

        getTableColumns() {            
            try {
                if (!this.config.table?.columns) {
                    console.error('❌ No table columns config');
                    return [];
                }
                
                const columns = this.config.table.columns;
                return columns;
            } catch (error) {
                console.error('❌ Error in getTableColumns:', error);
                return [];
            }
        },

        // 요약 필드 포맷팅
        getSummaryValue(field) {
            const value = this.data?.[field.key];
            return this.formatValue(value, 'currency');
        },

        // ⭐ 셀 값 포맷팅 (수정됨)
        getCellValue(item, column) {
            if (column.derived && column.formula) {
                // 파생 컬럼인 경우 formula 함수 실행
                const value = column.formula(item);
                return this.formatValue(value, column.format);
            } else {
                // 일반 컬럼인 경우 기존 로직
                const value = item[column.key];
                return this.formatValue(value, column.format);
            }
        },

        // ⭐ 셀 클래스 (수정됨)
        getCellClass(item, column) {
            let classes = []; // ⭐ classes 배열 초기화

            // 정렬 기준 추가
            if (column.align) {
                classes.push('text-' + column.align);
            }

            if (column.profit_loss) {
                const value = parseFloat(item[column.key]);
                if (!isNaN(value)) {
                    if (value > 0) {
                        classes.push('text-danger');
                    } else if (value < 0) {
                        classes.push('text-primary');
                    }
                }
            }

            // profit 형식이거나 파생 컬럼이 profit 관련인 경우 색상 적용
            if (column.format === 'profit' || column.key === '주당손익') {
                let value;
                if (column.derived && column.formula) {
                    value = column.formula(item);
                } else {
                    value = parseFloat(item[column.key]);
                }
                
                if (!isNaN(value)) {
                    if (value > 0) {
                        classes.push('text-danger');
                    } else if (value < 0) {
                        classes.push('text-primary');
                    }
                }
            }

            return classes.join(' ');
        },

        // 셀 클릭 핸들러
        // handleCellClick(item, column) {
        //     if (column.clickable) {
        //         console.log('Cell clicked:', item, column.key);
        //     }
        // },

        // API 호출
        async fetch_data() {
            this.loading = true;
            try {
                console.log('🔄 Fetching data...');
                const response = await callKiwoomApi(config.api_endpoint, config.payload);
                if (response.success) {
                    this.data = response.data;
                    this.return_code = response.data.return_code || 0;
                    this.return_msg = response.data.return_msg || '조회 성공';

                    console.log("✅ API로 데이터를 가져옴:", this.data);

                    // 콜백 함수들 실행
                    if (this.callbacks.length > 0) {
                        console.log(`📞 Executing ${this.callbacks.length} callback(s)...`);
                        for (const callback of this.callbacks) {
                            try {
                                await callback(this.data, this);
                            } catch (error) {
                                console.error('❌ Callback execution error:', error);
                            }
                        }
                        console.log('✅ All callbacks executed');
                    }

                    // Alpine.js의 nextTick 대신 setTimeout 사용
                    setTimeout(() => {
                        console.log("✅ fetch 후 DOM 갱신됨");
                        // Alpine.js 이벤트 디스패치
                        if (typeof this.$dispatch === 'function') {
                            this.$dispatch('data-updated');
                        }
                    }, 0);
                } else {
                    throw new Error(response.error_message || '알 수 없는 오류가 발생했습니다.');
                }
            } catch (err) {
                this.return_code = -1;
                this.return_msg = '오류: ' + err.message;
                console.error(`API 호출 오류:`, err);
            } finally {
                this.loading = false;
            }
        },

        // CSV 내보내기
        exportCSV() {
            const filename = `${config.title}_${new Date().toISOString().split('T')[0]}.csv`;
            let filtered_sorted_data = this.getSortedItems();
            window.KiwoomUtils.exportToCSV(filtered_sorted_data, config.table.columns, filename);
        },

        // 수동 새로고침
        refresh() {
            this.fetch_data();
        },

        // 자동 새로고침 토글
        toggleAutoRefresh() {
            if (window.KiwoomUtils.autoRefreshManager.timers[config.api_endpoint]) {
                window.KiwoomUtils.autoRefreshManager.stop(config.api_endpoint);
            } else {
                window.KiwoomUtils.autoRefreshManager.start(
                    config.api_endpoint,
                    () => this.fetch_data(),
                    config.auto_refresh
                );
            }
        },

        // action_buttons
        hasActionButtons() {
            return config.action_buttons && config.action_buttons.length > 0;
        },

        getActions(){
            return config.action_buttons;
        }
    };
};
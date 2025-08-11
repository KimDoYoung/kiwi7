/**
 * KiwoomBase 생성자
 * 
 * @param {*} config 
 * @returns 
 */
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
        
        // 캐시 : sorted_items 용
        _cached_items: null,
        _cache_key: '',        
        
        // 필터 관련 속성 추가
        filter_functions: [],  // 필터 함수들을 배열로 저장
        
        // 콜백 관련 속성 추가
        callbacks: [],  // 데이터 fetch 후 실행할 콜백 함수들

        config,  // 설정 객체 내부 보관용
 
        init() {
            this.fetch_data();

            if (config.auto_refresh) {
                // console.log(`🔁 Starting auto-refresh for ${configKey} every ${config.auto_refresh} ms`);
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
            
            // 해시를 숫자로 변환 (처음 8바이트만 사용)
            const hashArray = new Uint32Array(hashBuffer.slice(0, 8));
            return hashArray[0] ^ hashArray[1]; // XOR로 32비트로 축소
        },
        // 정렬
        sortBy(key) {
            if (this.sort_key === key) {
                this.sort_asc = !this.sort_asc;
            } else {
                this.sort_key = key;
                this.sort_asc = true;
            }
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
        // 캐쉬 clear
        clearCache(){
            this._cache_key=undefined;
            this._cached_items=undefined;
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

        // 활성 필터 개수
        get activeFilterCount() {
            return this.filter_functions.length;
        },

        // 데이터에서 배열 찾기 : data는 항목들 과 list로 구성된다.
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
            // 데이터가 없거나 로딩 중이면 빈 배열 반환
            if (!this.data || this.loading) {
                console.log('❌ No data or loading, returning empty array');
                return [];
            }
            
            // 데이터가 있을 때만 캐시 키 생성
            // const dataHash = this.data ? JSON.stringify(this.data).length : 0; // 간단한 해시 대용
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

        //
        // 필터링 + 정렬된 아이템 가져오기 (기존 get_sorted_items 수정)
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
                    // 모든 필터 함수를 통과해야 함
                    return this.filter_functions.every(filterFunc => {
                        try {
                            return filterFunc(item);
                        } catch (error) {
                            console.error('❌ Filter function error:', error);
                            return true; // 에러 시 통과시킴
                        }
                    });
                });
                console.log(`🔍 Filtered ${items.length} → ${filteredItems.length} items using ${this.filter_functions.length} filter(s)`);
            }

            // 2. 정렬 적용
            const sortedItems = window.KiwoomUtils.sortArray([...filteredItems], this.sort_key, this.sort_asc);
            console.log(`✅ Returning ${sortedItems.length} items (${this.filter_functions.length} filters applied, sorted: ${this.sort_key})`);
            
            return sortedItems;
        },

        // 필터링된 총 개수 (정렬 전)
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

        // 전체 아이템 개수 (필터링 전)
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
            return window.KiwoomUtils.formatValue(value, 'currency');
        },

        // 셀 값 포맷팅
        getCellValue(item, column) {
            const value = item[column.key];
            return window.KiwoomUtils.formatValue(value, column.format);
        },

        // 셀 클래스
        getCellClass(item, column) {
            if (column.profit_loss) {
                return window.KiwoomUtils.getProfitLossClass(item[column.key]);
            }
            return column.color_class || '';
        },

        // 셀 클릭 핸들러
        handleCellClick(item, column) {
            if (column.clickable) {
                console.log('Cell clicked:', item, column.key);
            }
        },

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

                    this.$nextTick(() => {
                        console.log("✅ fetch 후 DOM 갱신됨");
                        this.$dispatch('data-updated');
                    });
                } else {
                    throw new Error(response.error_message || '알 수 없는 오류가 발생했습니다.');
                }
            } catch (err) {
                this.return_code = -1;
                this.return_msg = '오류: ' + err.message;
                // console.error(`[${configKey}] API 호출 오류:`, err);
            } finally {
                this.loading = false;
            }
        },

        // CSV 내보내기 (필터링된 데이터로)
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
        }
    };
};
// static/js/components/kiwoom-base.js
window.KiwoomBase = function(configKey) {
    const config = window.KiwoomConfigs[configKey];
    if (!config) {
        throw new Error(`Config not found for key: ${configKey}`);
    }

    return {
        // 상태
        name: "홍길동",
        data: null,
        return_code: 0,
        return_msg: null,
        loading: false,
        sort_key: config.table.columns.find(col => col.sortable)?.key || config.table.columns[0].key,
        sort_asc: true,
        summary_full: false,
        _config: config,
        
        // 초기화
        async init() {
            this.fetch_data();
            
            // 자동 새로고침 설정
            if (config.auto_refresh) {
                console.log(`Starting auto-refresh for ${configKey} every ${config.auto_refresh} ms`);
                window.KiwoomUtils.autoRefreshManager.start(
                    configKey, 
                    () => this.fetch_data(), 
                    config.auto_refresh
                );
            }

            // 페이지 언로드 시 타이머 정리
            window.addEventListener('beforeunload', () => {
                window.KiwoomUtils.autoRefreshManager.stopAll();
            });
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

        // 데이터에서 배열 찾기 (fallback 함수)
        findArrayInData() {
            if (!this.data) return null;
            
            // 1. 설정된 키로 먼저 시도
            const configKey = this._config.table.data_key;
            if (this.data[configKey] && Array.isArray(this.data[configKey])) {
                return this.data[configKey];
            }
            
            // 2. 모든 키를 순회하며 배열 찾기
            for (const [key, value] of Object.entries(this.data)) {
                if (Array.isArray(value) && value.length > 0) {
                    console.log(`🔍 Found array at key: ${key} with ${value.length} items`);
                    return value;
                }
            }
            
            return null;
        },

        // 정렬된 아이템 (debugger 제거하고 로깅 추가)
        get sorted_items() {
            console.log('🔍 sorted_items getter called', {
                loading: this.loading,
                data: this.data,
                data_key: this._config.table.data_key,
                data_keys: this.data ? Object.keys(this.data) : 'no data'
            });
            
            // 로딩 중이거나 데이터가 없으면 빈 배열 반환
            if (this.loading || !this.data) {
                console.log('❌ No data or loading, returning empty array');
                return [];
            }
            
            // 데이터 구조 상세 분석
            console.log('📊 Data structure analysis:', {
                dataKeys: Object.keys(this.data),
                configDataKey: this._config.table.data_key,
                dataAtKey: this.data[this._config.table.data_key]
            });
            console.log('this._config.table.data_key:', this._config.table.data_key);
            // 먼저 설정된 키로 시도
            let items = this.data[this._config.table.data_key];
            
            // 설정된 키로 찾을 수 없으면 자동으로 배열 찾기
            if (!items || !Array.isArray(items)) {
                console.warn('⚠️ Configured key not found, searching for arrays...');
                items = this.findArrayInData();
            }
            
            if (!items || !Array.isArray(items)) {
                console.warn('❌ Items not found or not array:', {
                    items: items,
                    type: typeof items,
                    isArray: Array.isArray(items),
                    availableKeys: Object.keys(this.data)
                });
                return [];
            }

            const sortedItems = window.KiwoomUtils.sortArray([...items], this.sort_key, this.sort_asc);
            console.log('✅ Returning sorted items:', sortedItems.length, 'items');
            return sortedItems;
        },

        // 요약 필드 포맷팅
        getSummaryValue(field) {
            const value = this.data?.[field.key];
            return window.KiwoomUtils.formatValue(value, 'currency');
        },

        // 테이블 셀 값 포맷팅
        getCellValue(item, column) {
            const value = item[column.key];
            return window.KiwoomUtils.formatValue(value, column.format);
        },

        // 테이블 셀 클래스
        getCellClass(item, column) {
            if (column.profit_loss) {
                return window.KiwoomUtils.getProfitLossClass(item[column.key]);
            }
            return column.color_class || '';
        },

        // 셀 클릭 핸들러 (오버라이드 가능)
        handleCellClick(item, column) {
            if (column.clickable) {
                console.log('Cell clicked:', item, column.key);
                // 하위 클래스에서 오버라이드
            }
        },

        // API 호출 (강제 반응성 업데이트 추가)
        async fetch_data() {
            this.loading = true;
            try {
                console.log('🔄 Fetching data...');
                const response = await callKiwoomApi(config.api_endpoint, config.payload);
                if (response.success) {
                    // 데이터 업데이트
                    this.data = response.data;
                    this.return_code = response.data.return_code || 0;
                    this.return_msg = response.data.return_msg || '조회 성공';
                    this.name = "이순신";
                    
                    console.log("✅ API로 데이터를 가져옴:", this.data);
                    
                    // Alpine.js 강제 업데이트
                    this.$nextTick(() => {
                        console.log("✅ fetch 후 DOM 갱신됨");
                        // 강제로 반응성 트리거
                        this.$dispatch('data-updated');
                    });
                } else {
                    throw new Error(response.error_message || '알 수 없는 오류가 발생했습니다.');
                }
            } catch (err) {
                this.return_code = -1;
                this.return_msg = '오류: ' + err.message;
                console.error(`[${configKey}] API 호출 오류:`, err);
            } finally {
                this.loading = false;
            }
        },

        // CSV 내보내기
        exportCSV() {
            const filename = `${config.title}_${new Date().toISOString().split('T')[0]}.csv`;
            window.KiwoomUtils.exportToCSV(this.sorted_items, config.table.columns, filename);
        },

        // 수동 새로고침
        refresh() {
            this.fetch_data();
        },

        // 자동 새로고침 토글
        toggleAutoRefresh() {
            if (window.KiwoomUtils.autoRefreshManager.timers[configKey]) {
                window.KiwoomUtils.autoRefreshManager.stop(configKey);
            } else {
                window.KiwoomUtils.autoRefreshManager.start(
                    configKey, 
                    () => this.fetch_data(), 
                    config.auto_refresh
                );
            }
        }
    };
};
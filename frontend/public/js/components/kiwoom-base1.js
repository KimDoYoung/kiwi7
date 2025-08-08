// static/js/components/kiwoom-base.js
window.KiwoomBase = function(configKey) {
    const config = window.KiwoomConfigs[configKey];
    if (!config) {
        throw new Error(`Config not found for key: ${configKey}`);
    }

    return {
        data: null,
        return_code: 0,
        return_msg: null,
        loading: false,
        sort_key: config.table.columns.find(col => col.sortable)?.key || config.table.columns[0].key,
        sort_asc: true,
        summary_full: false,

        config,  // 설정 객체 내부 보관용

        // 초기화
        async init() {
            await this.fetch_data();

            if (config.auto_refresh) {
                console.log(`🔁 Starting auto-refresh for ${configKey} every ${config.auto_refresh} ms`);
                window.KiwoomUtils.autoRefreshManager.start(
                    configKey,
                    () => this.fetch_data(),
                    config.auto_refresh
                );
            }

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

        get_sorted_items (){
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
            const sortedItems = window.KiwoomUtils.sortArray([...items], this.sort_key, this.sort_asc);
            console.log('✅ Returning sorted items:', sortedItems.length, 'items');
            return sortedItems;

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
                console.error(`[${configKey}] API 호출 오류:`, err);
            } finally {
                this.loading = false;
            }
        },

        // CSV 내보내기
        exportCSV() {
            const filename = `${config.title}_${new Date().toISOString().split('T')[0]}.csv`;
            let sorted_data = this.get_sorted_items()
            window.KiwoomUtils.exportToCSV(sorted_data, config.table.columns, filename);
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

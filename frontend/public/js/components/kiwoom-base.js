// static/js/components/kiwoom-base.js
window.KiwoomBase = function(configKey) {
    const config = window.KiwoomConfigs[configKey];
    if (!config) {
        throw new Error(`Config not found for key: ${configKey}`);
    }

    return {
        // 상태
        data: null,
        return_code: 0,
        return_msg: null,
        loading: false,
        sort_key: config.table.columns.find(col => col.sortable)?.key || config.table.columns[0].key,
        sort_asc: true,
        summary_full: false,

        // 초기화
        init() {
            this.fetch_data();
            
            // 자동 새로고침 설정
            if (config.auto_refresh) {
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

        // 정렬된 아이템
        get sorted_items() {
            const items = this.data?.[config.table.data_key];
            if (!items || !Array.isArray(items)) return [];

            return window.KiwoomUtils.sortArray([...items], this.sort_key, this.sort_asc);
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

        // API 호출
        async fetch_data() {
            this.loading = true;
            try {
                const response = await callKiwoomApi(config.api_endpoint, config.payload);
                if (response.success) {
                    this.data = response.data;
                    this.return_code = response.data.return_code || 0;
                    this.return_msg = response.data.return_msg || '조회 성공';
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
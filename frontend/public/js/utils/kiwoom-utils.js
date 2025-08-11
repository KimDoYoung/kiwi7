// static/js/utils/kiwoom-utils.js
window.KiwoomUtils = {
    // 값 포맷팅
    formatValue(value, format) {
        if (value === null || value === undefined || value === '') return '';
        
        const numValue = Number(value); 
        
        switch (format) {
            case 'number':
                return numValue.toLocaleString();
            case 'currency':
                return numValue.toLocaleString() + ' 원';
            case 'percent':
                return value + ' %';
            case 'profit':
                const formattedValue = numValue.toLocaleString();
                return numValue >= 0 ? '+' + formattedValue : formattedValue;                
            default:
                return value;
        }
    },

    // 손익 색상 클래스
    getProfitLossClass(value) {
        const num = Number(value);
        if (num > 0) return 'text-danger';
        if (num < 0) return 'text-primary';
        return '';
    },

    // 정렬 함수
    sortArray(array, key, ascending = true) {
        return array.sort((a, b) => {
            let valA = a[key];
            let valB = b[key];

            // 숫자인 경우
            if (!isNaN(parseFloat(valA)) && !isNaN(parseFloat(valB))) {
                valA = parseFloat(valA);
                valB = parseFloat(valB);
            }

            if (valA < valB) return ascending ? -1 : 1;
            if (valA > valB) return ascending ? 1 : -1;
            return 0;
        });
    },

    // CSV 내보내기
    exportToCSV(data, columns, filename) {
        if (!data || !data.length) {
            alert('내보낼 데이터가 없습니다.');
            return;
        }

        const headers = columns.map(col => col.label).join(',');
        const rows = data.map(item => 
            columns.map(col => {
                let value;
                if (col.derived && col.formula) {
                    try {
                        value = col.formula(item);
                        // 포맷팅 적용
                        if (col.format) {
                            value = this.formatValue(value, col.format);
                        }
                    } catch (error) {
                        console.error(`Error calculating derived column ${col.key}:`, error);
                        value = '';
                    }
                } else {
                    // 일반 컬럼 처리
                    value = item[col.key] || '';
                }
                
                // CSV를 위해 콤마가 포함된 값은 따옴표로 감싸기
                if (typeof value === 'string' && (value.includes(',') || value.includes('"'))) {
                    value = `"${value.replace(/"/g, '""')}"`;  // 따옴표 이스케이프 처리
                }
                return value;
            }).join(',')
        ).join('\n');

        const csv = '\uFEFF' + headers + '\n' + rows; // UTF-8 BOM 추가
        const blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
        
        const link = document.createElement('a');
        const url = URL.createObjectURL(blob);
        link.setAttribute('href', url);
        link.setAttribute('download', filename || 'data.csv');
        link.style.visibility = 'hidden';
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    },

    // 자동 새로고침 관리
    autoRefreshManager: {
        timers: {},
        
        start(id, callback, interval) {
            this.stop(id); // 기존 타이머 정리
            this.timers[id] = setInterval(callback, interval);
        },
        
        stop(id) {
            if (this.timers[id]) {
                clearInterval(this.timers[id]);
                delete this.timers[id];
            }
        },
        
        stopAll() {
            Object.keys(this.timers).forEach(id => this.stop(id));
        }
    }
};
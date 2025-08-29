// ka01690 component – uses qry_dt (YYYYMMDD) and renders summary + per-stock rows
(function () {
    function profitKa01690() {
        return {
            qryDate: window.format_end_ymd ? window.format_end_ymd.replace(/(\d{4})-(\d{2})-(\d{2})/, '$1-$2-$3') : '',
            rawJson: '',
            summary: {},
            records: [],

            _toYYYYMMDD(d) {
                if (!d) return '';
                // accept Date or yyyy-mm-dd
                if (d instanceof Date) {
                    const y = d.getFullYear();
                    const m = String(d.getMonth() + 1).padStart(2, '0');
                    const dd = String(d.getDate()).padStart(2, '0');
                    return `${y}${m}${dd}`;
                }
                return d.replace(/-/g, '');
            },

            async search() {
                const qry_dt = this._toYYYYMMDD(this.qryDate);
                if (!qry_dt) {
                    this.rawJson = '조회일자를 선택하세요.';
                    return;
                }

                const payload = { qry_dt };
                try {
                    const res = await callKiwoomApi('ka01690', payload);
                    this.rawJson = JSON.stringify(res, null, 2);
                    console.log('ka01690 response', res);
                    // normalize and populate
                    if (res && res.success) {
                        const data = res.data || {};

                        // summary fields at top-level (prefer Korean keys from the example)
                        this.summary = {
                            tot_buy_amt: data['총 매입가'] || data.tot_buy_amt || data['총 매수금액'] || '',
                            tot_evlt_amt: data['총 평가금액'] || data.tot_evlt_amt || '',
                            tot_evltv_prft: data['총 평가손익'] || data.tot_evltv_prft || '',
                            tot_prft_rt: data['수익률'] || data.tot_prft_rt || '',
                            dbst_bal: data['예수금'] || data.dbst_bal || '',
                            est_assets: data['추정자산'] || data.est_assets || '',
                            buy_wght: data['매수비중'] || data.buy_wght || ''
                        };

                        // records: prefer explicit '일별잔고수익률' array, then fallbacks
                        let arr = [];
                        if (Array.isArray(data)) arr = data;
                        else if (Array.isArray(data['일별잔고수익률'])) arr = data['일별잔고수익률'];
                        else if (Array.isArray(data['일별잔고수익률'.replace(/\s/g, '')])) arr = data['일별잔고수익률'.replace(/\s/g, '')];
                        else if (Array.isArray(data.day_bal_rt)) arr = data.day_bal_rt;
                        else {
                            for (const v of Object.values(data)) {
                                if (Array.isArray(v)) { arr = v; break; }
                            }
                        }

                        // normalize per-item keys to match the example's Korean labels
                        this.records = (arr || []).map(item => ({
                            dt: item.dt || item['일자'] || data['일자'] || '',
                            cur_prc: item['현재가'] || item.cur_prc || '',
                            stk_cd: item['종목코드'] || item.stk_cd || '',
                            stk_nm: item['종목명'] || item.stk_nm || '',
                            rmnd_qty: item['보유 수량'] || item['보유수량'] || item.rmnd_qty || '',
                            buy_uv: item['매입 단가'] || item['매입단가'] || item.buy_uv || '',
                            buy_wght: item['매수비중'] || item.buy_wght || '',
                            evltv_prft: item['평가손익'] || item.evltv_prft || '',
                            prft_rt: item['수익률'] || item.prft_rt || '',
                            evlt_amt: item['평가금액'] || item.evlt_amt || '',
                            evlt_wght: item['평가비중'] || item.evlt_wght || ''
                        }));
                    } else {
                        this.summary = {};
                        this.records = [];
                    }
                } catch (e) {
                    console.error('ka01690 search error', e);
                    this.rawJson = '요청 오류: ' + (e && e.message ? e.message : String(e));
                    this.summary = {};
                    this.records = [];
                }
            },

            reset() {
                this.qryDate = window.format_end_ymd || '';
                this.rawJson = '';
                this.summary = {};
                this.records = [];
            },

            formatNumber(v) {
                if (v === null || v === undefined || v === '') return '-';
                const n = Number(String(v).replace(/[,\s]/g, ''));
                if (Number.isNaN(n)) return String(v);
                return n.toLocaleString();
            }
        };
    }

    document.addEventListener('alpine:init', () => {
        Alpine.data('profitKa01690', profitKa01690);
    });
})();

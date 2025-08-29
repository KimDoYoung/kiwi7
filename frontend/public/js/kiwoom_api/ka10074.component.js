// Simple Alpine component for ka10074 (일자별실현손익)
// This file intentionally keeps logic straightforward: fetch via callKiwoomApi and normalize Korean keys.
(function () {
    function profitKa10074() {
        return {
            filter: { strt_dt: window.format_start_ymd || null, end_dt: window.format_end_ymd || null },
            records: [],
            summary: { tot_buy_amt: 0, tot_sell_amt: 0, rlzt_pl: 0, trde_cmsn: 0, trde_tax: 0 },

            async searchProfit() {
                const payload = {
                    strt_dt: this.filter.strt_dt ? this.filter.strt_dt.replace(/-/g, '') : null,
                    end_dt: this.filter.end_dt ? this.filter.end_dt.replace(/-/g, '') : null
                };

                try {
                    const res = await callKiwoomApi('ka10074', payload);
                    if (res && res.success && res.data) {
                        const data = res.data;
                        const norm = {
                            tot_buy_amt: data['총매수금액'] ?? data['총 매수금액'] ?? 0,
                            tot_sell_amt: data['총매도금액'] ?? data['총 매도금액'] ?? 0,
                            rlzt_pl: data['실현손익'] ?? 0,
                            trde_cmsn: data['매매수수료'] ?? 0,
                            trde_tax: data['매매세금'] ?? 0,
                            dt_rlzt_pl: data['일자별실현손익'] ?? []
                        };

                        this.summary.tot_buy_amt = norm.tot_buy_amt;
                        this.summary.tot_sell_amt = norm.tot_sell_amt;
                        this.summary.rlzt_pl = norm.rlzt_pl;
                        this.summary.trde_cmsn = norm.trde_cmsn;
                        this.summary.trde_tax = norm.trde_tax;

                        let rows = [];
                        if (Array.isArray(norm.dt_rlzt_pl)) {
                            rows = norm.dt_rlzt_pl.map(r => ({
                                dt: r['일자'],
                                buy_amt: r['매수금액'],
                                sell_amt: r['매도금액'],
                                tdy_sel_pl: r['당일매도손익'],
                                tdy_trde_cmsn: r['당일매매수수료'],
                                tdy_trde_tax: r['당일매매세금']
                            }));
                        } else if (Array.isArray(data)) {
                            rows = data;
                        }

                        this.records = rows;
                    } else {
                        this.records = [];
                        this.summary = { tot_buy_amt: 0, tot_sell_amt: 0, rlzt_pl: 0, trde_cmsn: 0, trde_tax: 0 };
                    }
                } catch (e) {
                    console.error('ka10074 searchProfit error', e);
                    this.records = [];
                }
            },

            resetFilters() {
                this.filter = { strt_dt: '', end_dt: '' };
                this.searchProfit();
            },

            formatYmd(val) {
                if (!val) return '-';
                const s = String(val);
                if (s.length === 8) return s.slice(0,4) + '-' + s.slice(4,6) + '-' + s.slice(6,8);
                if (s.length >= 10 && s.includes('-')) return s.slice(0,10);
                return s;
            },

            formatNumber(val) {
                if (val === null || val === undefined || val === '') return '-';
                const n = Number(String(val).replace(/,/g, ''));
                if (Number.isNaN(n)) return val;
                return n.toLocaleString();
            },

            init() {
                this.searchProfit();
            }
        };
    }

    document.addEventListener('alpine:init', () => {
        Alpine.data('profitKa10074', profitKa10074);
    });
})();

// ka10085 component – 계좌수익율
(function () {
    function profitKa10085() {
        return {
            stexTp: '0',
            records: [],

            async search() {
                const payload = { stex_tp: this.stexTp };
                try {
                    const res = await callKiwoomApi('ka10085', payload);
                    console.log('ka10085 response', res);
                    if (res && res.success) {
                        const data = res.data || {};
                        // prefer acnt_prft_rt array
                        // let arr = [];
                        // if (Array.isArray(data.acnt_prft_rt)) arr = data.acnt_prft_rt;
                        // else if (Array.isArray(data.acnt_prft_rt)) arr = data.acnt_prft_rt;
                        // else {
                        //     for (const v of Object.values(data)) {
                        //         if (Array.isArray(v)) { arr = v; break; }
                        //     }
                        // }

                        // this.records = (arr || []).map(item => ({
                        //     dt: item.dt || item['일자'] || '',
                        //     stk_cd: item.stk_cd || item['종목코드'] || '',
                        //     stk_nm: item.stk_nm || item['종목명'] || '',
                        //     rmnd_qty: item.rmnd_qty || item['보유수량'] || item['보유 수량'] || '',
                        //     pur_pric: item.pur_pric || item['매입가'] || item['매입 단가'] || '',
                        //     pur_amt: item.pur_amt || item['매입금액'] || item['매입 금액'] || '',
                        //     cur_prc: item.cur_prc || item['현재가'] || '',
                        //     tdy_sel_pl: item.tdy_sel_pl || item['당일매도손익'] || item['당일손익'] || '',
                        //     prft_rt: item.prft_rt || item['수익률'] || ''
                        // }));
                        this.records = data['계좌수익률'] || [];
                    } else {
                        this.records = [];
                    }
                } catch (e) {
                    console.error('ka10085 search error', e);
                    this.records = [];
                }
            },

            reset() {
                this.stexTp = '0';
                this.records = [];
            },

            formatNumber(v) {
                if (v === null || v === undefined || v === '') return '-';
                const n = Number(String(v).replace(/[,%\s]/g, ''));
                if (Number.isNaN(n)) return String(v);
                return n.toLocaleString();
            },

            calcPrftRt(r) {
                // prefer returned prft_rt, else compute if possible
                if (r.prft_rt && r.prft_rt !== '') return r.prft_rt;
                const cur = Number(String(r.cur_prc).replace(/[,\s]/g, ''));
                const pur = Number(String(r.pur_pric || r.pur_pric).replace(/[,\s]/g, ''));
                if (!cur || !pur) return '-';
                return ((cur - pur) / pur * 100).toFixed(2) + '%';
            }
        };
    }

    document.addEventListener('alpine:init', () => {
        Alpine.data('profitKa10085', profitKa10085);
    });
})();

function kt00016Component() {
    return {
        fr_dt: '', // 시작일
        to_dt: '', // 종료일
    loading: false,
    error: '',
    summary: {},
    message: '',
        init() {
            // 기본값: 오늘 날짜로 설정
            const today = new Date();
            const ymd = today.toISOString().slice(0, 10);
            this.fr_dt = ymd;
            this.to_dt = ymd;
        },
        async fetchData() {
            this.loading = true;
            this.error = '';
            this.summary = {};
            this.message = '';
            try {
                const payload = {};
                if (this.fr_dt) payload.fr_dt = this.fr_dt.replace(/-/g, '');
                if (this.to_dt) payload.to_dt = this.to_dt.replace(/-/g, '');

                const res = await callKiwoomApi('kt00016', payload);
                if (res && res.success && res.data && typeof res.data === 'object' && !Array.isArray(res.data)) {
                    // 주요 항목만 추출
                    const keys = [
                        "관리사원번호", "관리자명", "관리자지점",
                        "예수금_초", "예수금_말", "유가증권평가금액_초", "유가증권평가금액_말",
                        "순자산액계_초", "순자산액계_말", "투자원금평잔", "평가손익", "수익률", "회전율"
                    ];
                    this.summary = {};
                    keys.forEach(k => { if (res.data[k] !== undefined) this.summary[k] = res.data[k]; });
                    this.message = res.data.return_msg || '';
                } else {
                    this.summary = {};
                    this.message = '데이터를 불러올 수 없습니다.';
                }
            } catch (e) {
                this.error = '서버 오류: ' + (e && e.message ? e.message : String(e));
                this.summary = {};
                this.message = '';
            } finally {
                this.loading = false;
            }
        },
        formatNumber(val) {
            if (!val) return '';
            return Number(val).toLocaleString();
        }
    }
}

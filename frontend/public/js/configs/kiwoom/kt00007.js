// 체결내역 페이지 설정
const kt00007 = {
    title: '체결내역',
    api_endpoint: 'kt00007',
    action_buttons: [],
    payload: {
        ord_dt: '20250825', // 주문일자 (YYYYMMDD)
        qry_tp: '4', // 4:체결내역만
        stk_bond_tp: '0', // 0:전체
        sell_tp: '0', // 0:전체
        stk_cd: '', // 종목코드
        fr_ord_no: '', // 시작주문번호
        dmst_stex_tp: '%' // %(전체)
    },
    table: {
        data_key: '계좌별주문체결내역상세',
        columns: [
            { key: '주문번호', label: '주문번호', sortable: true },
            { key: '종목명', label: '종목명', sortable: true },
            { key: '종목코드', label: '종목코드', sortable: true },
            { key: '주문구분', label: '주문구분', sortable: true },
            { key: '매매구분', label: '매매구분', sortable: true },
            { key: '주문수량', label: '주문수량', format: 'number', sortable: true },
            { key: '주문단가', label: '주문단가', format: 'number', sortable: true },
            { key: '체결수량', label: '체결수량', format: 'number', sortable: true },
            { key: '체결단가', label: '체결단가', format: 'number', sortable: true },
            { key: '주문시간', label: '주문시간', format: 'time', sortable: true },
            { key: '확인수량', label: '확인수량', format: 'number', sortable: true },
            { key: '확인시간', label: '확인시간', format: 'time', sortable: true }
        ]
    },
    auto_refresh: 0 // 자동 새로고침 비활성화
};

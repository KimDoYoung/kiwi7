// KIS 주식잔고조회 설정
const tttc8434r = {
    title: '계좌평가현황(KIS)',
    api_endpoint: 'TTTC8434R',
    action_buttons: ['buy', 'sell', 'detail'],
    payload: {
        // 기본 조회 조건
        inqr_dvsn: "02" // 01:대출일별, 02:종목별
    },
    summary: {
        basic_fields: [
            { key: '예수금총금액', label: '예수금' },
            { key: '총평가금액', label: '총평가금액' },
            { key: '매입금액합계금액', label: '총매입금액' },
            { key: '평가손익합계금액', label: '총평가손익', profit_loss: true },
            { key: '유가평가금액', label: '유가평가액' },
            { key: '익일정산금액', label: 'D+1예수금' }
        ],
        extended_fields: [
            { key: '총대출금액', label: '총대출금' },
            { key: '자산증감액', label: '자산증감', profit_loss: true },
            { key: '순자산금액', label: '순자산' }
        ]
    },
    table: {
        data_key: 'output1',
        columns: [
            { key: '상품번호', label: '종목코드', sortable: true, clickable: true },
            { key: '상품명', label: '종목명', sortable: true, clickable: true },
            { key: '보유수량', label: '보유수량', sortable: true, format: 'number' },
            { key: '매입평균가격', label: '평균단가', sortable: true, format: 'number' },
            { key: '현재가', label: '현재가', sortable: true, format: 'number' },
            // 파생 컬럼: 주당순익
            {
                key: '주당손익',
                label: '1주당',
                sortable: true,
                align: 'right',
                format: 'profit',
                derived: true,
                formula: (item) => {
                    const price = parseFloat(item.현재가) || 0;
                    const avg = parseFloat(item.매입평균가격) || 0;
                    return price - avg;
                }
            },
            { key: '평가금액', label: '평가금액', sortable: true, format: 'number' },
            { key: '평가손익금액', label: '손익금액', sortable: true, format: 'number', profit_loss: true },
            { key: '평가손익율', label: '손익율', sortable: true, format: 'percent', profit_loss: true },
            { key: '매입금액', label: '매입금액', sortable: true, format: 'number' },
            { key: '주문가능수량', label: '주문가능', sortable: true, format: 'number' }
        ]
    },
    auto_refresh: 0
};

// LS 주식잔고조회 설정
const t0424 = {
    title: '계좌평가현황(LS)',
    api_endpoint: 't0424',
    action_buttons: ['buy', 'sell', 'detail'],
    payload: {
        qry_tp: "0"
    },
    summary: {
        basic_fields: [
            { key: '예수금', label: '예수금' },
            { key: '출금가능금액', label: '출금가능' },
            { key: '잔고평가금액', label: '총평가금' },
            { key: '평가손익합계', label: '총평가손익', profit_loss: true },
            { key: '총매입금액', label: '총매입' },
            { key: '예탁자산총액', label: '총자산' }
        ],
        extended_fields: [
            { key: '투자원금', label: '투자원금' },
            { key: '손익율', label: '총수익율', profit_loss: true }
        ]
    },
    table: {
        data_key: 't0424OutBlock1',
        columns: [
            { key: '종목번호', label: '종목번호', sortable: true, clickable: true },
            { key: '종목명', label: '종목명', sortable: true, clickable: true },
            { key: '잔고수량', label: '보유수량', sortable: true, format: 'number' },
            { key: '평균단가', label: '평균단가', sortable: true, format: 'number' },
            { key: '현재가', label: '현재가', sortable: true, format: 'number' },
            // 파생 컬럼: 주당손익
            {
                key: '주당손익',
                label: '1주당',
                sortable: true,
                align: 'right',
                format: 'profit',
                derived: true,
                formula: (item) => {
                    const price = parseFloat(item.현재가) || 0;
                    const avg = parseFloat(item.평균단가) || 0;
                    return price - avg;
                }
            },
            { key: '평가금액', label: '평가금액', sortable: true, format: 'number' },
            { key: '평가손익', label: '손익금액', sortable: true, format: 'number', profit_loss: true },
            { key: '수익율', label: '손익율', sortable: true, format: 'percent', profit_loss: true },
            { key: '매도가능수량', label: '주문가능', sortable: true, format: 'number' }
        ]
    },
    auto_refresh: 0
};

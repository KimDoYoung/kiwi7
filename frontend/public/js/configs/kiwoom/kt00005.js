// 체결잔고요청 페이지 설정
const kt00005 = {
    title: '체결잔고요청',
    api_endpoint: 'kt00005',
    action_buttons: ['buy', 'sell', 'detail'],
    payload: {
        dmst_stex_tp: "KRX"
    },
    summary: {
        basic_fields: [
            { key: '예수금', label: '예수금' },
            { key: '예수금D+1', label: '예수금D+1' },
            { key: '예수금D+2', label: '예수금D+2' },
            { key: '출금가능금액', label: '출금가능금액' },
            { key: '주문가능현금', label: '주문가능현금' },
            { key: '평가금액합계', label: '평가금액합계' }
        ],
        extended_fields: [
            { key: '미수확보금', label: '미수확보금' },
            { key: '대용금', label: '대용금' },
            { key: '권리대용금', label: '권리대용금' },
            { key: '현금미수금', label: '현금미수금' },
            { key: '신용이자미납금', label: '신용이자미납금' },
            { key: '기타대여금', label: '기타대여금' },
            { key: '미상환융자금', label: '미상환융자금' },
            { key: '증거금현금', label: '증거금현금' },
            { key: '증거금대용', label: '증거금대용' },
            { key: '주식매수총액', label: '주식매수총액' },
            { key: '총손익합계', label: '총손익합계', color_class: 'text-danger' },
            { key: '총손익률', label: '총손익률', color_class: 'text-danger' },
            { key: '총재매수가능금액', label: '총재매수가능금액' },
            { key: '20%주문가능금액', label: '20%주문가능금액' },
            { key: '30%주문가능금액', label: '30%주문가능금액' },
            { key: '40%주문가능금액', label: '40%주문가능금액' },
            { key: '50%주문가능금액', label: '50%주문가능금액' },
            { key: '60%주문가능금액', label: '60%주문가능금액' },
            { key: '100%주문가능금액', label: '100%주문가능금액' },
            { key: '신용융자합계', label: '신용융자합계' },
            { key: '신용융자대주합계', label: '신용융자대주합계' },
            { key: '신용담보비율', label: '신용담보비율' },
            { key: '예탁담보대출금액', label: '예탁담보대출금액' },
            { key: '매도담보대출금액', label: '매도담보대출금액' }
        ]
    },
    table: {
        data_key: '종목별체결잔고',
        columns: [
            { key: '종목번호', label: '종목코드', sortable: true, clickable: true },
            { key: '종목명', label: '종목명', sortable: true, clickable: true },
            { key: '신용구분', label: '신용구분', sortable: true },
            { key: '대출일', label: '대출일', sortable: true },
            { key: '만기일', label: '만기일', sortable: true },
            { key: '결제잔고', label: '결제잔고', sortable: true, format: 'number' },
            { key: '현재잔고', label: '현재잔고', sortable: true, format: 'number' },
            { key: '현재가', label: '현재가', sortable: true, format: 'number' },
            { key: '매입단가', label: '매입단가', sortable: true, format: 'number' },
            // 👇 파생 컬럼 추가
            { 
                key: '주당손익', 
                label: '1주당', 
                sortable: true, 
                align: 'right', 
                format: 'profit',
                derived: true,  // 파생 컬럼 표시
                formula: (item) => {
                    const 현재가 = parseInt(item.현재가, 10) || 0;
                    const 매입단가 = parseInt(item.매입단가, 10) || 0;
                    return 현재가 - 매입단가;
                }
            },
            { key: '매입금액', label: '매입금액', sortable: true, format: 'number' },
            { key: '평가금액', label: '평가금액', sortable: true, format: 'number' },
            { key: '평가손익', label: '평가손익', sortable: true, format: 'number', profit_loss: true },
            { key: '손익률', label: '손익률', sortable: true, format: 'percent', profit_loss: true }
        ]
    },
    auto_refresh: 0 // 0이면 자동 refresh 비활성화, 3000이면 3초
};
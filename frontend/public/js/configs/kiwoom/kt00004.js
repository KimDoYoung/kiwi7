// 계좌잔고 페이지 설정
const kt00004 ={
        title: '계좌평가현황',
        api_endpoint: 'kt00004',
        action_buttons: ['buy', 'sell', 'detail'],
        payload: {
            qry_tp: "0",
            dmst_stex_tp: "KRX"
        },
        summary: {
            basic_fields: [
                { key: '예수금', label: '예수금' },
                { key: 'D+2추정예수금', label: 'D+2추정예수금' },
                { key: '유가잔고평가액', label: '유가잔고평가액' },
                { key: '예탁자산평가액', label: '예탁자산평가액' },
                { key: '총매입금액', label: '총매입금액' },
                { key: '추정예탁자산', label: '추정예탁자산' }
            ],
            extended_fields: [
                { key: '매도담보대출금', label: '매도담보대출금' },
                { key: '당일투자원금', label: '당일투자원금' },
                { key: '당월투자원금', label: '당월투자원금' },
                { key: '누적투자원금', label: '누적투자원금' },
                { key: '당일투자손익', label: '당일투자손익', color_class: 'text-danger' },
                { key: '당월투자손익', label: '당월투자손익', color_class: 'text-danger' },
                { key: '누적투자손익', label: '누적투자손익', color_class: 'text-danger' },
                { key: '당일손익율', label: '당일손익율' },
                { key: '당월손익율', label: '당월손익율' },
                { key: '누적손익율', label: '누적손익율' }
            ]
        },
        table: {
            data_key: '종목별계좌평가현황',
            columns: [
                { key: '종목코드', label: '종목코드', sortable: true, clickable: true },
                { key: '종목명', label: '종목명', sortable: true, clickable: true },
                { key: '전일대비', label: '전일대비', sortable: true, format: 'number' ,
                  derived: true,
                  formula: (item) => {
                      const 현재가 = parseInt(item.현재가, 10) || 0;
                        const 전일종가 = parseInt(item.전일종가, 10) || 0;
                        return 현재가 - 전일종가;
                    }  
                },
                { key: '평균단가', label: '매입평단', sortable: true, format: 'number' },
                { key: '현재가', label: '현재가', sortable: true, format: 'number' },
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
                        const 평균단가 = parseInt(item.평균단가, 10) || 0;
                        return 현재가 - 평균단가;
                    }
                },                
                { key: '보유수량', label: '보유수량', sortable: true, format: 'number' },
                { key: '보유비중', label: '보유비중(%)', sortable: true, format: 'percent' },
                { key: '매입금액', label: '매입금액', sortable: true, format: 'number' },
                { key: '평가금액', label: '평가금액', sortable: true, format: 'number' },
                { key: '손익율', label: '손익율', sortable: true, format: 'percent', profit_loss: true },
                { key: '손익금액', label: '손익금액', sortable: true, format: 'number', profit_loss: true },
                { key: '가격추세', label: '최근추세', sortable: false }
            ]
        },
        auto_refresh: 0 //0이면 자동 refresh 비활성화, 3000이면 3초
    };
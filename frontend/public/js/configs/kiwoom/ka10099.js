// 계좌잔고 페이지 설정
const ka10099 ={
        title: '종목정보리스트',
        api_endpoint: 'ka10099',
        action_buttons: [],
        payload: {
            "mrkt_tp" : "0"
        },
        summary: {
        },
        table: {
            data_key: '종목리스트',
            columns: [
                //{ key: '종목코드', label: '종목코드', sortable: true, clickable: true },
            ]
        },
        auto_refresh: 0 //0이면 자동 refresh 비활성화, 3000이면 3초
    };
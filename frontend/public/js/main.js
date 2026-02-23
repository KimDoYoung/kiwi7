    function mainApp() {
        return {
            init() {
                console.log('mainApp initialized');
                // 초기화 코드 작성
            },
            run() {
                console.log('mainApp running');
                // 실행 코드 작성
            },
            logout() {
                localStorage.removeItem('kiwi7_token');
                sessionStorage.removeItem('kiwi7_token');
                window.location.href = "/kiwi7/logout"; // 서버 로그아웃 (쿠키 삭제 및 리디렉션)
            }
        };
    }
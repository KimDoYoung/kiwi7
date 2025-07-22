/**
 * 로그인 페이지용 Alpine.js 함수 (초보자용 - 매우 간단)
 */
function loginApp() {
    return {
        // 데이터 (상태)
        showPassword: false,
        isLoading: false,
        errorMessage: '',
        
        /**
         * 로그인 함수 - 폼 제출 시 호출됩니다
         */
        async login() {
            console.log('로그인 함수 호출됨');
            
            // 로딩 시작
            this.isLoading = true;
            this.errorMessage = '';
            
            // 폼 데이터 가져오기 (간단한 방법)
            const userId = document.getElementById('userId').value;
            const password = document.getElementById('password').value;
            
            // 기본 검증
            if (!userId || !password) {
                this.errorMessage = '아이디와 비밀번호를 입력하세요.';
                this.isLoading = false;
                return;
            }
            
            try {
                // FormData로 POST 요청 (기존 백엔드와 호환)
                const formData = new FormData();
                formData.append('userId', userId);
                formData.append('password', password);
                
                const response = await fetch('/login', {
                    method: 'POST',
                    body: formData
                });
                
                if (response.ok) {
                    // 로그인 성공
                    const result = await response.json();
                    console.log('로그인 성공:', result);
                    
                    // 메인 페이지로 이동
                    window.location.href = '/main';
                } else {
                    // 로그인 실패
                    const error = await response.json();
                    this.errorMessage = error.detail || '로그인에 실패했습니다.';
                }
                
            } catch (error) {
                console.error('로그인 오류:', error);
                this.errorMessage = '네트워크 오류가 발생했습니다.';
            }
            
            // 로딩 종료
            this.isLoading = false;
        },
        
        /**
         * 테스트 계정 자동입력
         */
        fillTestAccount() {
            document.getElementById('userId').value = 'admin';
            document.getElementById('password').value = '1234';
            this.errorMessage = '';
        }
    }
}
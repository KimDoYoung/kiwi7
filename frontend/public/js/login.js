/**
 * 로그인 페이지용 Alpine.js 함수 (초보자용 - 매우 간단)
 */
function loginApp() {
    return {
        // 데이터 (상태)
        showPassword: false,
        isLoading: false,
        errorMessage: '',
        password: '', // 4자리 비밀번호 저장 (문자열로 초기화)
        
        // Alpine.js 초기화 함수
        init() {
            console.log('Alpine.js 초기화됨');
            this.password = ''; // 명시적 초기화
        },
        
        /**
         * 숫자 패드에서 숫자 클릭 시 호출
         * @param {number} num - 클릭된 숫자 (0-9)
         */
        addNumber(num) {
            // 4자리까지만 입력 가능
            if (this.password.length < 4) {
                this.password += num.toString();
                this.errorMessage = ''; // 에러 메시지 초기화
            }
        },
        
        /**
         * 백스페이스 버튼 클릭 시 마지막 숫자 제거
         */
        removeLastNumber() {
            if (this.password.length > 0) {
                this.password = this.password.slice(0, -1);
            }
        },
        
        /**
         * 클리어 버튼 클릭 시 모든 숫자 제거
         */
        clearPassword() {
            this.password = '';
            this.errorMessage = '';
        },
        
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
            const password = this.password; // Alpine.js 데이터에서 가져오기
            
            // 기본 검증
            if (!userId || !password) {
                this.errorMessage = '아이디와 비밀번호를 입력하세요.';
                this.isLoading = false;
                return;
            }
            
            // 비밀번호 4자리 검증
            if (password.length !== 4) {
                this.errorMessage = '비밀번호는 4자리 숫자여야 합니다.';
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
            this.password = '1234'; // Alpine.js 데이터로 설정
            this.errorMessage = '';
        }
    }
}
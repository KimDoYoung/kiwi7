/**
 * 로그인 페이지 Alpine.js 애플리케이션
 * POST /login 엔드포인트로 인증 요청을 처리합니다.
 */
function loginApp() {
    return {
        // 로그인 폼 데이터
        loginForm: {
            userId: '',
            password: '',
            rememberMe: false
        },
        
        // UI 상태 관리
        isLoading: false,
        showPassword: false,
        errorMessage: '',
        successMessage: '',
        showDemoInfo: true, // 개발 환경에서는 true
        
        /**
         * 로그인 폼 제출 처리
         * POST /login 엔드포인트로 인증 요청을 보냅니다.
         */
        async login() {
            // 기본 유효성 검사
            if (!this.loginForm.userId.trim()) {
                this.showError('사용자 아이디를 입력하세요.');
                return;
            }
            
            if (!this.loginForm.password.trim()) {
                this.showError('비밀번호를 입력하세요.');
                return;
            }
            
            this.isLoading = true;
            this.clearMessages();
            
            try {
                // POST /login 엔드포인트로 로그인 요청
                const response = await fetch('/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json'
                    },
                    body: JSON.stringify({
                        user_id: this.loginForm.userId,
                        password: this.loginForm.password,
                        remember_me: this.loginForm.rememberMe
                    })
                });
                
                const result = await response.json();
                
                if (response.ok) {
                    // 로그인 성공 처리
                    this.handleLoginSuccess(result);
                } else {
                    // 로그인 실패 처리
                    this.handleLoginError(result);
                }
                
            } catch (error) {
                console.error('로그인 요청 오류:', error);
                this.showError('네트워크 오류가 발생했습니다. 다시 시도해 주세요.');
            } finally {
                this.isLoading = false;
            }
        },
        
        /**
         * 로그인 성공 시 처리
         */
        handleLoginSuccess(result) {
            this.showSuccess('로그인이 성공했습니다!');
            
            // 토큰 저장 (localStorage 또는 쿠키)
            if (result.access_token) {
                if (this.loginForm.rememberMe) {
                    localStorage.setItem('kiwi7_token', result.access_token);
                } else {
                    sessionStorage.setItem('kiwi7_token', result.access_token);
                }
            }
            
            // 리다이렉트 처리
            setTimeout(() => {
                const redirectUrl = new URLSearchParams(window.location.search).get('redirect') || '/';
                window.location.href = redirectUrl;
            }, 1500);
        },
        
        /**
         * 로그인 실패 시 처리
         */
        handleLoginError(result) {
            const errorMessage = result.detail || result.message || '로그인에 실패했습니다.';
            this.showError(errorMessage);
            
            // 비밀번호 필드 초기화
            this.loginForm.password = '';
        },
        
        /**
         * 데모 계정 정보 자동 입력
         */
        fillDemoCredentials() {
            this.loginForm.userId = 'demo';
            this.loginForm.password = 'demo123';
            this.clearMessages();
        },
        
        /**
         * 오류 메시지 표시
         */
        showError(message) {
            this.errorMessage = message;
            this.successMessage = '';
        },
        
        /**
         * 성공 메시지 표시
         */
        showSuccess(message) {
            this.successMessage = message;
            this.errorMessage = '';
        },
        
        /**
         * 모든 메시지 초기화
         */
        clearMessages() {
            this.errorMessage = '';
            this.successMessage = '';
        },
        
        /**
         * 페이지 로드 시 초기화
         */
        init() {
            console.log('로그인 앱 초기화 완료');
            
            // 이미 로그인된 사용자 체크
            const token = localStorage.getItem('kiwi7_token') || sessionStorage.getItem('kiwi7_token');
            if (token) {
                // 토큰 유효성 검사 후 리다이렉트
                this.validateTokenAndRedirect(token);
            }
            
            // 엔터 키 이벤트 처리
            this.setupKeyboardEvents();
        },
        
        /**
         * 토큰 유효성 검사 및 리다이렉트
         */
        async validateTokenAndRedirect(token) {
            try {
                const response = await fetch('/api/v1/auth/verify', {
                    headers: {
                        'Authorization': `Bearer ${token}`
                    }
                });
                
                if (response.ok) {
                    window.location.href = '/';
                }
            } catch (error) {
                // 토큰이 유효하지 않으면 제거
                localStorage.removeItem('kiwi7_token');
                sessionStorage.removeItem('kiwi7_token');
            }
        },
        
        /**
         * 키보드 이벤트 설정
         */
        setupKeyboardEvents() {
            document.addEventListener('keydown', (event) => {
                // Ctrl+Enter로 빠른 로그인 (개발용)
                if (event.ctrlKey && event.key === 'Enter' && this.showDemoInfo) {
                    this.fillDemoCredentials();
                    setTimeout(() => this.login(), 100);
                }
            });
        }
    }
}
// 전역 상태 관리
   window.kiwiGlobal = window.kiwiGlobal || {
       selectedStockCode: null
   };

   function cleanStockCode(stk_code){
       return stk_code.replace(/[^0-9]/g, '');
   }
   /**
    * 종목코드를 기반으로 회사 정보를 하단의 canvas에 표시합니다.
    * @param {string} stk_code - 종목코드
    */
   async function showCompanyCanvas(stk_code) {
        const cleanCode = cleanStockCode(stk_code);
        console.log("showCompanyCanvas:", cleanCode);

        // offcanvas 요소 찾기
        const companyCanvas = document.getElementById('offcanvasCompany');
        if (!companyCanvas) {
            console.error('offcanvasCompany element not found');
            return;
        }

        // 로딩 상태 표시
        showCompanyLoading(true);

        try {
            const url = `/kiwi7/api/v1/stock/info/${cleanCode}`;
            const response = await getFetch(url);
            
            if (response.success && response.data) {
                console.log("회사 정보:", response.data);
                renderCompanyInfo(response.data);
                showCompanyOffcanvas();
            } else {
                throw new Error(response.error_message || '주식 정보를 가져올 수 없습니다.');
            }
        } catch (error) {
            console.error('회사 정보 조회 오류:', error);
            showCompanyError(error.message);
        } finally {
            showCompanyLoading(false);
        }
    }

    /**
     * 회사 정보를 렌더링합니다.
     * @param {Object} data - API에서 받은 주식 데이터
     */
    function renderCompanyInfo(data) {
        // 제목 설정
        const title = `${data.종목명} (${data.종목코드})`;
        updateElement('#offcanvasCompanyName', title);

        // 현재가 정보
        const currentPrice = parseInt(data.현재가?.replace(/[^0-9-]/g, '')) || 0;
        const prevDiff = parseInt(data.전일대비?.replace(/[^0-9-]/g, '')) || 0;
        const changeRate = parseFloat(data.등락율) || 0;
        
        updateElement('#current-price', formatNumber(Math.abs(currentPrice)));
        updateElement('#price-diff', formatPriceDiff(prevDiff));
        updateElement('#change-rate', `${changeRate}%`);
        
        // 가격 색상 적용
        const priceColor = prevDiff > 0 ? 'text-red-500' : prevDiff < 0 ? 'text-blue-500' : 'text-base-content';
        document.querySelector('#current-price')?.setAttribute('class', `text-2xl font-bold ${priceColor}`);
        document.querySelector('#price-diff')?.setAttribute('class', `${priceColor}`);
        document.querySelector('#change-rate')?.setAttribute('class', `${priceColor}`);

        // 거래 정보
        updateElement('#volume', formatNumber(parseInt(data.거래량) || 0));
        updateElement('#high-price', formatNumber(parseInt(data.고가?.replace(/[^0-9]/g, '')) || 0));
        updateElement('#low-price', formatNumber(parseInt(data.저가?.replace(/[^0-9]/g, '')) || 0));
        updateElement('#open-price', formatNumber(parseInt(data.시가?.replace(/[^0-9]/g, '')) || 0));

        // 기업 정보
        updateElement('#market-cap', data.시가총액 ? `${formatNumber(parseInt(data.시가총액))}억` : '-');
        updateElement('#shares', data.상장주식 ? `${formatNumber(parseInt(data.상장주식))}만주` : '-');
        
        // 재무 정보
        updateElement('#per', data.PER || '-');
        updateElement('#pbr', data.PBR || '-');
        updateElement('#eps', data.EPS ? formatNumber(parseInt(data.EPS)) : '-');
        updateElement('#bps', data.BPS ? formatNumber(parseInt(data.BPS)) : '-');
        updateElement('#roe', data.ROE ? `${data.ROE}%` : '-');

        // 52주 최고/최저
        updateElement('#year-high', formatNumber(parseInt(data.연중최고?.replace(/[^0-9]/g, '')) || 0));
        updateElement('#year-low', formatNumber(parseInt(data.연중최저?.replace(/[^0-9]/g, '')) || 0));

        // 우측 영역 - 기업 개요
        updateElement('#company-summary', data.company_summary || '기업 개요 정보가 없습니다.');
        
        // 우측 영역 - 기업 상세 정보
        updateElement('#market-name', data.시장명 || '-');
        updateElement('#sector-name', data.업종명 || '-');
        updateElement('#company-size', data.회사크기분류 || '-');
        updateElement('#company-type', data.회사분류 || '-');
        updateElement('#listing-date', formatDate(data.상장일) || '-');
        
        // 재무 상세 정보
        updateElement('#revenue', data.매출액 ? `${formatNumber(parseInt(data.매출액))}억` : '-');
        updateElement('#operating-profit', data.영업이익 ? `${formatNumber(parseInt(data.영업이익))}억` : '-');
        updateElement('#net-income', data.당기순이익 ? `${formatNumber(parseInt(data.당기순이익))}억` : '-');
        
        // 주식 상세 정보
        updateElement('#face-value', data.액면가 ? `${formatNumber(parseInt(data.액면가))}${data.액면가단위 || '원'}` : '-');
        updateElement('#capital', data.자본금 ? `${formatNumber(parseInt(data.자본금))}억` : '-');
        updateElement('#float-ratio', data.유통비율 ? `${data.유통비율}%` : '-');
        updateElement('#foreign-ownership', data.외인소진률 ? `${data.외인소진률}%` : '-');
        updateElement('#credit-ratio', data.신용비율 ? `${data.신용비율}%` : '-');
        
        // 투자 정보
        updateElement('#stock-status', data.종목상태 || '-');
        updateElement('#supervision-status', data.감리구분 || '-');
        updateElement('#nxt-available', data.NXT가능여부 === 'Y' ? '가능' : '불가능');
        
        // 250일 최고/최저 (있는 경우)
        if (data['250최고']) {
            updateElement('#high-250', formatNumber(parseInt(data['250최고']?.replace(/[^0-9]/g, '')) || 0));
            updateElement('#high-250-date', formatDate(data['250최고가일']));
            updateElement('#high-250-ratio', `${data['250최고가대비율']}%`);
            document.getElementById('high-250-card')?.classList.remove('hidden');
        }
        if (data['250최저']) {
            updateElement('#low-250', formatNumber(parseInt(data['250최저']?.replace(/[^0-9]/g, '')) || 0));
            updateElement('#low-250-date', formatDate(data['250최저가일']));
            updateElement('#low-250-ratio', `${data['250최저가대비율']}%`);
            document.getElementById('low-250-card')?.classList.remove('hidden');
        }
    }

    /**
     * 날짜를 포맷합니다 (YYYYMMDD -> YYYY-MM-DD)
     */
    function formatDate(dateString) {
        if (!dateString || dateString.length !== 8) return dateString;
        return `${dateString.substring(0, 4)}-${dateString.substring(4, 6)}-${dateString.substring(6, 8)}`;
    }

    /**
     * 회사 정보 offcanvas를 표시합니다.
     */
    function showCompanyOffcanvas() {
        const toggle = document.getElementById('company-info-toggle');
        if (toggle) {
            toggle.checked = true;
        }
    }

    /**
     * 로딩 상태를 표시/숨김합니다.
     */
    function showCompanyLoading(show) {
        const loadingEl = document.getElementById('company-loading');
        if (loadingEl) {
            loadingEl.style.display = show ? 'block' : 'none';
        }
    }

    /**
     * 오류 메시지를 표시합니다.
     */
    function showCompanyError(message) {
        updateElement('#offcanvasCompanyName', '정보 조회 실패');
        updateElement('#company-error', `오류: ${message}`);
        showCompanyOffcanvas();
    }

    /**
     * DOM 요소의 텍스트를 안전하게 업데이트합니다.
     */
    function updateElement(selector, text) {
        const element = document.querySelector(selector);
        if (element) {
            element.textContent = text;
        }
    }

    /**
     * 숫자를 천 단위 구분자와 함께 포맷합니다.
     */
    function formatNumber(num) {
        return Number(num).toLocaleString();
    }

    /**
     * 가격 차이를 포맷합니다.
     */
    function formatPriceDiff(diff) {
        if (diff > 0) return `+${formatNumber(diff)}`;
        if (diff < 0) return formatNumber(diff);
        return '0';
    }
    // 오른쪽에서 나오는 매수/매도 offcanvas를 보이게 하는 함수
    function showBuySellCanvas(params = {}) {
        const {
            stk_code = '',
            stk_name = '',
            which = '', // '매수', '매도', 또는 빈 문자열
            qty = 1,
            cost = 0
        } = params;

        console.log('showBuySellCanvas called with:', params);

        // offcanvas 요소 찾기 (DaisyUI Drawer Toggle)
        const drawerToggle = document.getElementById('buy-sell-drawer-toggle');
        if (!drawerToggle) {
            console.error('buy-sell-drawer-toggle element not found');
            return;
        }

        // 폼 데이터 설정
        try {
            // 매수/매도 섹션 요소 찾기
            const buySection = document.getElementById('offcanvasBuy');
            const sellSection = document.getElementById('offcanvasSell');
            const buyForm = document.getElementById('buy-form');
            const sellForm = document.getElementById('sell-form');

            // 공통 데이터 설정 (매수/매도 폼 모두에)
            [buyForm, sellForm].forEach(form => {
                if (form) {
                    const pdnoInput = form.querySelector('input[name="pdno"]');
                    const pdnmInput = form.querySelector('input[name="pdnm"]');
                    const qtyInput = form.querySelector('input[name="qty"]');
                    const costInput = form.querySelector('input[name="cost"]');

                    if (pdnoInput) pdnoInput.value = stk_code;
                    if (pdnmInput) pdnmInput.value = stk_name;
                    if (qtyInput) qtyInput.value = qty;
                    if (costInput) costInput.value = cost;
                }
            });

            // 매수/매도 모드에 따른 섹션 표시/숨김
            if (which === '매수') {
                showSection(buySection);
                hideSection(sellSection);
                clearForm(sellForm);
            } else if (which === '매도') {
                showSection(sellSection);
                hideSection(buySection);
                clearForm(buyForm);
            } else {
                // 둘 다 표시
                showSection(buySection);
                showSection(sellSection);
            }

        } catch (error) {
            console.error('Error setting up buy/sell form:', error);
        }

        // offcanvas 표시
        drawerToggle.checked = true;
    }

    // 섹션 표시 헬퍼 함수
    function showSection(section) {
        if (!section) return;
        section.classList.remove('hidden');
        section.style.display = 'block'; // fallback
    }

    // 섹션 숨김 헬퍼 함수
    function hideSection(section) {
        if (!section) return;
        section.classList.add('hidden');
        section.style.display = 'none'; // fallback
    }

    // 폼 초기화 헬퍼 함수
    function clearForm(form) {
        if (!form) return;
        const inputs = form.querySelectorAll('input');
        inputs.forEach(input => {
            if (input.type !== 'radio' && input.type !== 'checkbox') {
                input.value = '';
            }
        });
    }
    //toast 에러메세지 표시
    function showToastError(error) {
        const statusCode = error.status || 'Error';
        const detail = error.detail || error.message || '알 수 없는 오류가 발생했습니다.';
        
        console.error(`Toast Error: [${statusCode}] ${detail}`);

        const toast = document.getElementById('toastError');
        const codeEl = document.getElementById('error-status-code');
        const detailEl = document.getElementById('error-detail');

        if (toast && codeEl && detailEl) {
            codeEl.textContent = statusCode;
            detailEl.textContent = detail;
            
            toast.classList.remove('hidden');
            
            // 5초 후 자동으로 닫기
            if (toast.hideTimer) clearTimeout(toast.hideTimer);
            toast.hideTimer = setTimeout(() => {
                toast.classList.add('hidden');
            }, 5000);
        } else {
            // Toast 요소가 없으면 alertfallback
            alert(`오류가 발생했습니다: \n${detail} (${statusCode})`);
        }
    }
    
    // 범용 Alert 함수 - 다양한 유형의 Alert 표시 (Tailwind/DaisyUI)
    function showAlert(message, type = 'info', duration = 5000) {
        const alertConfig = {
            success: {
                class: 'alert-success',
                icon: 'bi-check-circle-fill',
                prefix: '성공'
            },
            error: {
                class: 'alert-error',
                icon: 'bi-exclamation-triangle-fill',
                prefix: '오류'
            },
            warning: {
                class: 'alert-warning',
                icon: 'bi-exclamation-triangle-fill',
                prefix: '경고'
            },
            info: {
                class: 'alert-info',
                icon: 'bi-info-circle-fill',
                prefix: '알림'
            }
        };

        const config = alertConfig[type] || alertConfig.error;
        const $alert = document.getElementById('alert');
        const $alertIcon = document.getElementById('alertIcon');
        const $alertStatus = document.getElementById('alertStatus');
        const $alertMessage = document.getElementById('alertMessage');

        if (!$alert || !$alertIcon || !$alertStatus || !$alertMessage) {
            console.error('Alert elements not found');
            return;
        }

        // Alert 스타일 초기화 (기본 클래스 보존)
        $alert.className = `alert shadow-lg pointer-events-auto flex justify-between ${config.class}`;
        $alertIcon.className = `bi ${config.icon} text-2xl shrink-0`;
        $alertStatus.textContent = config.prefix;
        $alertMessage.textContent = message;

        // Alert 표시
        $alert.classList.remove('hidden');

        // 지정된 시간 후 자동으로 숨김
        if (duration > 0) {
            // 기존 타이머 제거
            if ($alert.hideTimer) clearTimeout($alert.hideTimer);
            
            $alert.hideTimer = setTimeout(() => {
                hideAlert();
            }, duration);
        }
    }

    // Alert 숨김 함수
    function hideAlert() {
        const $alert = document.getElementById('alert');
        if ($alert) {
            $alert.classList.add('hidden');
        }
    }

    // 기존 showAlertError 함수 - 호환성 유지하면서 showAlert 사용
    function showAlertError(error) {
        const statusCode = error.status;
        const detail = error.detail || error.message;
        const message = statusCode ? `[${statusCode}] ${detail}` : detail;
        
        showAlert(message, 'error', 5000);
    }
/**
 * document ready 이벤트 핸들러 등록
 */
document.addEventListener('DOMContentLoaded', function() {
    // 매수 폼 submit 처리
    const buyForm = document.getElementById('buy-form');
    if (buyForm) {
        buyForm.addEventListener('submit', handleBuySubmit);
    }
    
    // 매도 폼 submit 처리  
    const sellForm = document.getElementById('sell-form');
    if (sellForm) {
        sellForm.addEventListener('submit', handleSellSubmit);
    }
    
    // 매수/매도 canvas 초기화 버튼들 처리
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('btnClearBuySell')) {
            handleClearBuySell(e);
        }
    });

    updateTodayTime();
    setInterval(updateTodayTime, 1000);
});
// 실시간 날짜/시간 표시
function updateTodayTime() {
    const days = ['일', '월', '화', '수', '목', '금', '토'];
    const now = new Date();
    const yyyy = now.getFullYear();
    const mm = String(now.getMonth() + 1).padStart(2, '0');
    const dd = String(now.getDate()).padStart(2, '0');
    const hh = String(now.getHours()).padStart(2, '0');
    const min = String(now.getMinutes()).padStart(2, '0');
    const ss = String(now.getSeconds()).padStart(2, '0');
    const dayKor = days[now.getDay()];
    const formatted = `${yyyy}-${mm}-${dd} ${hh}:${min}:${ss} (${dayKor})`;
    const el = document.getElementById('span_today_time');
    if (el) el.textContent = formatted;
}
// 매수 처리 함수
async function processBuyOrder({ market, pdno, pdnm, qty, cost }) {
    console.log('매수 주문 처리 시작:', {market, pdno, pdnm, qty, cost });
    
    const payload = {
        dmst_stex_tp: market,
        stk_cd: cleanStockCode(pdno),
        ord_qty: String(qty), // qty를 string으로 변환
        ord_uv:  String(cost || 0),
        trde_tp: '0', // 매수
        cond_uv: ""
    };   if (payload.ord_uv == 0) {
        payload.trde_tp = "3" //시장가
    } 

    try {
        const response = await callKiwoomApi('kt10000', payload);
        
        if (response.success) {
            const message = response.data?.return_msg || '매수 주문이 성공적으로 처리되었습니다.';
            showOrderResult('success', message);
            return { success: true, message };
        } else {
            throw new Error(response.error_message || '매수 주문 처리 실패');
        }
    } catch (error) {
        const errorMsg = error instanceof KiwiError ? 
            `에러 ${error.status}: ${error.message}` : 
            '매수 주문 오류: ' + error.message;
        
        console.error('매수 주문 오류:', error);
        showOrderResult('error', errorMsg);
        return { success: false, error: errorMsg };
    }
}

// 매도 처리 함수
async function processSellOrder({ market, pdno, pdnm, qty, cost }) {
    console.log('매도 주문 처리 시작:', {market, pdno, pdnm, qty, cost });
    
    const payload = {
        dmst_stex_tp: market,
        stk_cd: cleanStockCode(pdno),
        ord_qty: String(qty),
        ord_uv: String(cost || 0),
        trde_tp: '0', // 매도
        cond_uv: ""
    };

    if (payload.ord_uv == 0) {
        payload.trde_tp = "3" //시장가
    } 

    try {
        const response = await callKiwoomApi('kt10001', payload);
        
        if (response.success) {
            const message = response.data?.return_msg || '매도 주문이 성공적으로 처리되었습니다.';
            showOrderResult('success', message);
            return { success: true, message };
        } else {
            throw new Error(response.error_message || '매도 주문 처리 실패');
        }
    } catch (error) {
        const errorMsg = error instanceof KiwiError ? 
            `에러 ${error.status}: ${error.message}` : 
            '매도 주문 오류: ' + error.message;
        
        console.error('매도 주문 오류:', error);
        showOrderResult('error', errorMsg);
        return { success: false, error: errorMsg };
    }
}

// 주문 결과 표시 함수
function showOrderResult(type, message) {
    const messageArea = document.getElementById('buy-sell-message-area');
    if (!messageArea) return;

    const alertClass = type === 'success' ? 'alert-success' : 'alert-danger';
    const iconClass = type === 'success' ? 'fa-check-circle' : 'fa-exclamation-triangle';
    
    messageArea.innerHTML = `
        <div class="alert ${alertClass} alert-dismissible fade show" role="alert">
            <i class="fas ${iconClass} me-2"></i>
            ${message}
            <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
        </div>
    `;

    // 3초 후 자동 제거
    setTimeout(() => {
        const alert = messageArea.querySelector('.alert');
        if (alert) {
            alert.classList.remove('show');
            setTimeout(() => messageArea.innerHTML = '', 150);
        }
    }, 3000);
}

// 폼 데이터 추출 헬퍼 함수
function extractFormData(form) {
    const formData = new FormData(form);
    return {
        market: formData.get('market')?.trim() || 'KRX', // 기본값 KRX
        pdno: formData.get('pdno')?.trim(),
        pdnm: formData.get('pdnm')?.trim(),
        qty: parseInt(formData.get('qty')) || 0,
        cost: parseInt(formData.get('cost')) || 0
    };
}

// 매수 폼 submit 핸들러
async function handleBuySubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = extractFormData(form);
    
    // 폼 유효성 검사
    if (!formData.pdno || !formData.pdnm || formData.qty <= 0) {
        showOrderResult('error', '필수 입력 항목을 확인해주세요.');
        return;
    }

    // 버튼 비활성화
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>처리중...';

    try {
        await processBuyOrder(formData);
    } finally {
        // 버튼 복원
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
}

// 매도 폼 submit 핸들러
async function handleSellSubmit(e) {
    e.preventDefault();
    
    const form = e.target;
    const formData = extractFormData(form);
    
    // 폼 유효성 검사
    if (!formData.pdno || !formData.pdnm || formData.qty <= 0) {
        showOrderResult('error', '필수 입력 항목을 확인해주세요.');
        return;
    }

    // 버튼 비활성화
    const submitBtn = form.querySelector('button[type="submit"]');
    const originalText = submitBtn.textContent;
    submitBtn.disabled = true;
    submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>처리중...';

    try {
        await processSellOrder(formData);
    } finally {
        // 버튼 복원
        submitBtn.disabled = false;
        submitBtn.textContent = originalText;
    }
}

// 초기화 버튼 핸들러
function handleClearBuySell(e) {
    const button = e.target;
    const form = button.closest('form');
    
    if (form) {
        // 폼 초기화
        form.reset();
        
        // 읽기 전용 필드들도 초기화
        const readonlyInputs = form.querySelectorAll('input[readonly]');
        readonlyInputs.forEach(input => input.value = '');
        
        console.log('폼이 초기화되었습니다:', form.id);
    }
    
    // 메시지 영역 초기화
    const messageArea = document.getElementById('buy-sell-message-area');
    if (messageArea) {
        messageArea.innerHTML = '';
    }
}

/**
 * 매매일지 모달을 표시합니다.
 * 전역 변수 kiwiGlobal.selectedStockCode에 종목코드가 있으면 자동으로 설정됩니다.
 */
function showDiaryModal() {
    console.log('showDiaryModal 함수 호출됨');
    
    // 전역 변수에서 종목코드 확인
    const stkCd = window.kiwiGlobal?.selectedStockCode || null;
    if (stkCd) {
        console.log(`전역 변수에서 종목코드 발견: ${stkCd}`);
    } else {
        console.log('종목코드 없음 - 빈 폼으로 모달 열기');
    }
    
    try {
        const modalElement = document.getElementById('stkDiaryModal');
        if (modalElement) {
            console.log('모달 요소 발견, Bootstrap Modal 인스턴스 생성');
            
            // DaisyUI showModal
            if (typeof modalElement.showModal === "function") {
                modalElement.showModal();
            } else {
                console.error("Not a dialog element");
            }
            console.log('모달 표시 완료');
        } else {
            console.error('stkDiaryModal 요소를 찾을 수 없습니다.');
        }
    } catch (error) {
        console.error('모달 표시 중 오류 발생:', error);
        console.error('오류 스택:', error.stack);
    }
}

/**
 * 종목코드와 함께 매매일지 모달을 표시합니다.
 * @param {string} stkCd - 종목코드
 */
function showDiaryModalWithStock(stkCd) {
    if (stkCd) {
        window.kiwiGlobal.selectedStockCode = stkCd;
        console.log(`종목코드 ${stkCd}로 일지 모달 열기`);
    }
    showDiaryModal();
}

/**
 * 전역 종목코드를 설정합니다.
 * @param {string} stkCd - 종목코드
 */
function setSelectedStockCode(stkCd) {
    window.kiwiGlobal.selectedStockCode = stkCd;
    console.log(`전역 종목코드 설정: ${stkCd}`);
}

/**
 * 전역 종목코드를 초기화합니다.
 */
function clearSelectedStockCode() {
    window.kiwiGlobal.selectedStockCode = null;
    console.log('전역 종목코드 초기화');
}

/**
 * 매매일지 모달을 표시합니다. diary 객체가 전달되면 update 모드로 설정합니다.
 * @param {Object|null} diary - 수정할 일지 객체 (선택)
 */
function showDiaryModal(diary = null) {
    console.log('showDiaryModal 함수 호출됨', diary ? 'diary 전달됨' : '신규 작성');

    try {
        const modalElement = document.getElementById('stkDiaryModal');
        if (!modalElement) {
            console.error('stkDiaryModal 요소를 찾을 수 없습니다.');
            return;
        }

        // 모달 내부 Alpine 인스턴스에 diary 전달 시도
        const setDiaryOnAlpine = () => {
            // Alpine v3 stores component data on _x_dataStack
            const alpineInstance = modalElement._x_dataStack && modalElement._x_dataStack[0];
            if (alpineInstance && typeof alpineInstance.setDiary === 'function') {
                try {
                    alpineInstance.setDiary(diary);
                    console.log('Alpine 컴포넌트에 diary 설정 완료');
                    return true;
                } catch (e) {
                    console.warn('Alpine setDiary 호출 중 오류:', e);
                }
            }
            return false;
        };

        if (diary) {
            const ok = setDiaryOnAlpine();
            if (!ok) {
                // Alpine 인스턴스가 아직 준비되지 않았을 수 있으므로 커스텀 이벤트로 전달
                const ev = new CustomEvent('diary:open', { detail: diary });
                modalElement.dispatchEvent(ev);
                console.log('diary:open 이벤트로 diary 전달');
            }
        }

        if (typeof modalElement.showModal === "function") {
            modalElement.showModal();
        }
        console.log('모달 표시 완료');

    } catch (error) {
        console.error('모달 표시 중 오류 발생:', error);
        console.error('오류 스택:', error.stack);
    }
}

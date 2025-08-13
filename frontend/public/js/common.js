   function cleanStockCode(stk_code){
       return stk_code.replace(/[^0-9]/g, '');
   }
   function showCompanyCanvas(stk_code){
        // const url = '/api/v1/mystock/company-info/' + stk_code;
        // getFetch(url).then(data => {
        //     console.log(data); 
        //     const name_code = data.naver.stk_name + ' (' + data.naver.stk_code + ')';
        //     const $companyCanvas = $('#offcanvasCompany');
        //     $companyCanvas.find('#offcanvasCompanyName').text(name_code);
        //     $companyCanvas.find('#offcanvas-naver-company-summary').text(data.naver.company_summary);
        //     $companyCanvas.find('#offcanvas-naver-market-cap').text(data.naver.market_cap);
        //     $companyCanvas.find('#offcanvas-naver-market-cap-rank').text(data.naver.market_cap_rank);
        //     $companyCanvas.find('#offcanvas-naver-num-of-shares').text(data.naver.num_of_shares);
        //     //현재가
        //     let price_data = data.current_price.output;
        //     $companyCanvas.find('#offcanvas-stck_prpr').text(JuliaUtil.displayMoney(price_data.stck_prpr));
        //     $companyCanvas.find('#offcanvas-prdy_vrss').text(JuliaUtil.displayMoney(data.current_price.output.prdy_vrss));
        //     $companyCanvas.find('#offcanvas-prdy_ctrt').text(data.current_price.output.prdy_ctrt);
        //     $companyCanvas.find('#offcanvas-acml_vol').text(JuliaUtil.displayMoney(data.current_price.output.acml_vol));
        //     $companyCanvas.find('#offcanvas-acml_tr_pbmn').text(moneyFormat(data.current_price.output.acml_tr_pbmn));
        //     //candle chart
        //     const chart_data = data.price_history.output;
        //     let columns = [];
        //     let columns1 = ['data1'];
        //     let columns2 = ['x'];
        //     //시가,고가,저가,종가
        //     // debugger;
        //     for (let i = chart_data.length - 1; i >= 0; i--) {
        //         let item = chart_data[i];
        //         columns1.push([Number(item.stck_oprc), Number(item.stck_hgpr), Number(item.stck_lwpr), Number(item.stck_clpr)]);
        //         columns2.push(item.stck_bsop_date);
        //     }
        //     let start_ymd = columns2[1].substring(0, 4) + '-' + columns2[1].substring(4, 6) + '-' + columns2[1].substring(6, 8);
        //     let end_ymd = columns2[chart_data.length-1].substring(0, 4) + '-' + columns2[chart_data.length-1].substring(4, 6) + '-' + columns2[chart_data.length-1].substring(6, 8);
        //     let x_name = `${data.naver.stk_name} (${start_ymd}~${end_ymd})`;
        //     columns.push(columns1);
        //     //columns.push(columns2);
            
        //     offcanvasCompany.toggle();
        //     create_billboard_candle_chart("offcanvas_daily_chart",columns, x_name)
        // }).catch(error=> {
        //     console.error(error.message); 
        //     showAlertError(error);
        // });
        
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

        // offcanvas 요소 찾기
        const buySellCanvas = document.getElementById('offcanvasBuySell');
        if (!buySellCanvas) {
            console.error('offcanvasBuySell element not found');
            return;
        }

        // Bootstrap offcanvas 인스턴스 생성 또는 가져오기
        let offcanvasBuySell = bootstrap.Offcanvas.getInstance(buySellCanvas);
        if (!offcanvasBuySell) {
            offcanvasBuySell = new bootstrap.Offcanvas(buySellCanvas);
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
                document.getElementById('offcanvasExampleLabel').innerText = '매수';
            } else if (which === '매도') {
                showSection(sellSection);
                hideSection(buySection);
                clearForm(buyForm);
                document.getElementById('offcanvasExampleLabel').innerText = '매도';
            } else {
                // 둘 다 표시
                showSection(buySection);
                showSection(sellSection);
            }

        } catch (error) {
            console.error('Error setting up buy/sell form:', error);
        }

        // offcanvas 표시
        offcanvasBuySell.show();
    }

    // 섹션 표시 헬퍼 함수
    function showSection(section) {
        if (!section) return;
        section.style.display = 'block';
    }

    // 섹션 숨김 헬퍼 함수
    function hideSection(section) {
        if (!section) return;
        section.style.display = 'none';
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
        const statusCode = error.status;
        const detail = error.detail || error.message;
        // $('#toastError').find('#error-status-code').text(statusCode);
        // $('#toastError').find('#error-detail').text(detail);
        var toast = new bootstrap.Toast(document.getElementById('toastError'));
        $('.toast').toast({
                animation: false,
                delay: 1000
            });
        $('.toast').toast('show');
    }
    //alsert 에러메세지 표시
    function showAlertError(error) {
        const statusCode = error.status;
        const detail = error.detail || error.message;
        // const $alert = $('#alertError')
        // $alert.find('#alertErrorStatus').text(statusCode);
        // $alert.find('#alertErrorMessage').text(detail);
        // $alert.removeClass('d-none');
        // setTimeout(() => {
        //     $alert.addClass('d-none');
        // }, 5000);
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
});
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

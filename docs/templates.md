# templates

## html 템플릿

1. x-data의 이름을 바꾼다.

```html
{% extends 'common/base.html' %}
{% block style %}
{% endblock %}
{% block content %}
<div x-data="stock_find" class="container mt-4">
  <h2>테스트1</h2>
  <form @submit.prevent="submit" class="mb-4">
    <div class="row g-3">
      <div class="col-md-3">
        <label for="stkCode" class="form-label">API id</label>
        <input type="text" class="form-control" id="apiId" name="apiId" placeholder="ex) ka10100" x-model="apiId">
      </div>
      <div class="col-md-3">
        <label for="stkCode" class="form-label">종목코드</label>
        <input type="text" class="form-control" id="stkCode" name="stkCode" placeholder="005930" x-model="stkCode">
      </div>
      <div class="col-md-3">
        <label for="startDate" class="form-label">시작일</label>
        <input type="text" class="form-control" id="startDate" name="startDate" placeholder="YYYYMMDD" x-model="startDate">
      </div>
      <div class="col-md-3">
        <label for="endDate" class="form-label">종료일</label>
        <input type="text" class="form-control" id="endDate" name="endDate" placeholder="YYYYMMDD" x-model="endDate">
      </div>
    </div>
    <div class="mt-3">
      <button type="submit" class="btn btn-primary" :disabled="loading">
        <span x-show="loading" class="spinner-border spinner-border-sm me-2" role="status"></span>
        조회
      </button>
    </div>
  </form>
 <div x-text="msg"></div>
 <div x-text="data?.return_msg"></div>
  
  <!-- RAW -->
  <div x-show="view==='raw'">
    <div x-text="totalItemCount"></div>
    <pre class="bg-light p-2 border rounded mb-0" style="max-height: 60vh; overflow:auto;" x-text="raw"></pre>
  </div>    
</div>
{% raw %}
<!--handlebar scripts-->
{% endraw %}
{% endblock %}
{% block script %}
<script src="/public/js/configs/kiwoom/kt00004.js"></script>
<script src="/public/js/utils/kiwoom-utils.js"></script>
<script src="/public/js/components/kiwoom-base.js"></script>
<script>
document.addEventListener('alpine:init', () => {
    Alpine.data('stock_find', () => {
        let base = window.createKiwoomBase(kt00004, {
            callApi : callKiwoomApi,
            utils : window.KiwoomUtils,
            debug: false
        });
        return {
            ...base,
            view:'raw',
            raw: null,
            apiId:null,
            stkCode: null,
            startDate: null,
            endDate: null,
            msg:null,
            // data: null,
            init(){
                if(base.init) {
                    base.init.call(this);
                }
                this.addCallback((data)=>{
                    this.raw = JSON.stringify(data, null, 2);
                })
            },
            get total_item_count(){
                return this.totalItemCount() || 0;
            },
            async submit(){
                this.msg = null;
                if (!this.apiId) {
                    this.msg = "API id는 필수입니다.";
                    return;
                }
                let payload = {
                    "stk_cd" : this.stkCode
                }
                if (this.startDate) {
                    payload.strt_dt = this.startDate;
                }
                if (this.endDate) {
                    payload.end_date = this.endDate;
                }   
                await this.fetch_data(this.apiId, payload)
                    
                
                this.raw = JSON.stringify(this.data, null, 2);
            }
        }
    });

});
</script>
{% endblock %}
```

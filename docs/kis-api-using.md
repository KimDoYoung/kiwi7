# KIS(한국투자증권) API 사용 현황

Lucy 2.0에서 사용하는 KIS 증권 API 목록입니다.

## 파일 위치

| 파일 | 설명 |
|------|------|
| `backend/app/domains/stc/kis/kis_stock_api.py` | REST API 클라이언트 |
| `backend/app/domains/stc/kis/kis_ws_task.py` | WebSocket 처리 |
| `backend/app/utils/kis_ws_util.py` | WebSocket 유틸리티 |
| `backend/app/domains/stc/kis/model/` | 요청/응답 모델 (35개 파일) |

---

## REST API 목록

### 1. 시세 조회 API

#### 1.1 현재가 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST01010100` |
| **메서드** | `current_cost()`, `get_current_price()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/inquire-price` |
| **HTTP** | GET |
| **용도** | 단일 종목의 현재가 조회 |
| **요청** | `fid_cond_mrkt_div_code`: "J", `fid_input_iscd`: 종목코드 |
| **응답** | 현재가, 전일대비, 거래량 등 상세정보 |

#### 1.2 현재가 시세2
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHPST01010000` |
| **메서드** | `inquire_price_2()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/inquire-price-2` |
| **HTTP** | GET |
| **용도** | 추가 옵션이 있는 현재가 조회 |

#### 1.3 기간별 시세 (일/주/월/년)
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST03010100` |
| **메서드** | `inquire_daily_itemchartprice()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/intstock-stocklist-by-group` |
| **HTTP** | GET |
| **용도** | 기간별(일/주/월/년) 봉 차트 데이터 조회 |

#### 1.4 당일 분봉 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST03010200` |
| **메서드** | `inquire_time_itemchartprice()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/inquire-time-itemchartprice` |
| **HTTP** | GET |
| **용도** | 당일 분봉(시간별) 데이터 조회 |

#### 1.5 일자별 현재가
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST01010400` |
| **메서드** | `inquire_daily_price()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/inquire-daily-price` |
| **HTTP** | GET |
| **용도** | 과거 일별 현재가 데이터 조회 |

---

### 2. 주문 API

#### 2.1 현금 매수/매도
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC0802U` (매수), `TTTC0801U` (매도) |
| **메서드** | `order()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/order-cash` |
| **HTTP** | POST |
| **용도** | 현금 주문 (시장가/지정가) |
| **요청** | `buy_sell_gb`: 매수/매도, `stk_code`: 종목코드, `qty`: 수량, `cost`: 가격 (0=시장가) |
| **주문구분** | `ORD_DVSN`: "00"(지정가), "01"(시장가) |

#### 2.2 주문 취소
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC0803U` |
| **메서드** | `order_cancel()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/order-rvsecncl` |
| **HTTP** | POST |
| **용도** | 주문 취소 |
| **요청** | `RVSE_CNCL_DVSN_CD`: "02" (취소), `QTY_ALL_ORD_YN`: "Y" (전체취소) |

#### 2.3 주문 정정
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC0803U` |
| **메서드** | `order_modify()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/order-rvsecncl` |
| **HTTP** | POST |
| **용도** | 주문 정정 |
| **요청** | `RVSE_CNCL_DVSN_CD`: "01" (정정), `QTY_ALL_ORD_YN`: "N" |

---

### 3. 잔고/계좌 API

#### 3.1 주식 잔고 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC8434R` |
| **메서드** | `inquire_balance()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/inquire-balance` |
| **HTTP** | GET |
| **용도** | 보유 종목 및 현금 잔고 조회 |
| **응답** | `output1`: 보유종목 목록, `output2`: 현금 정보 |

#### 3.2 일별 주문 체결 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC8001R` |
| **메서드** | `inquire_daily_ccld()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/inquire-daily-ccld` |
| **HTTP** | GET |
| **용도** | 매매 거래 기록 조회 (3개월 이내) |
| **요청** | 조회기간, `sll_buy_dvsn_cd`: "00"(전체)/"01"(매도)/"02"(매수) |

#### 3.3 정정취소 가능수량 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC8036R` |
| **메서드** | `inquire_psbl_rvsecncl()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/inquire-psbl-rvsecncl` |
| **HTTP** | GET |
| **용도** | 정정/취소 가능한 주문수량 확인 |
| **주의** | 모의투자 사용 불가 |

#### 3.4 매수 가능 수량 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC8908R` |
| **메서드** | `inquire_psbl_order()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/inquire-psbl-order` |
| **HTTP** | GET |
| **용도** | 현금 및 신용잔고로 매수 가능한 수량 |

#### 3.5 매도 가능 수량 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC8408R` |
| **메서드** | `inquire_psbl_sell()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/inquire-psbl-sell` |
| **HTTP** | GET |
| **용도** | 보유 주식의 매도 가능수량 (담보제한 반영) |

#### 3.6 통합증거금 현황
| 항목 | 내용 |
|------|------|
| **TR CD** | `TTTC0869R` |
| **메서드** | `intgr_margin()` |
| **Endpoint** | `/uapi/domestic-stock/v1/trading/intgr-margin` |
| **HTTP** | GET |
| **용도** | 통합증거금 현황 및 신용한도 조회 |

---

### 4. 조건식 API

#### 4.1 조건식 목록 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `HHKST03900300` |
| **메서드** | `psearch_title()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/psearch-title` |
| **HTTP** | GET |
| **용도** | HTS에 저장된 조건식 목록 조회 |

#### 4.2 조건식 결과 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `HHKST03900400` |
| **메서드** | `psearch_result()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/psearch-result` |
| **HTTP** | GET |
| **용도** | 특정 조건식의 실행 결과 종목 조회 |

---

### 5. 관심종목 API

#### 5.1 관심종목 그룹 목록
| 항목 | 내용 |
|------|------|
| **TR CD** | `HHKCM113004C7` |
| **메서드** | `attension_grouplist()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/intstock-grouplist` |
| **HTTP** | GET |
| **용도** | HTS 관심종목 그룹 목록 조회 |

#### 5.2 그룹별 종목 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `HHKCM113004C6` |
| **메서드** | `attension_stocklist_by_group()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/intstock-stocklist-by-group` |
| **HTTP** | GET |
| **용도** | 특정 그룹의 관심종목 목록 |

#### 5.3 멀티종목 시세 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST11300006` |
| **메서드** | `attension_multi_price()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/intstock-multprice` |
| **HTTP** | GET |
| **용도** | 여러 종목의 현재가를 한 번에 조회 |

---

### 6. 종목정보/시장정보 API

#### 6.1 상품정보 검색
| 항목 | 내용 |
|------|------|
| **TR CD** | `CTPF1002R` |
| **메서드** | `search_stock_info()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/search-stock-info` |
| **HTTP** | GET |
| **용도** | 종목코드나 이름으로 종목 정보 검색 |

#### 6.2 휴장일 조회
| 항목 | 내용 |
|------|------|
| **TR CD** | `CTCA0903R` |
| **메서드** | `chk_workingday()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/chk-holiday` |
| **HTTP** | GET |
| **용도** | 특정 날짜가 휴장일인지 확인 |

#### 6.3 시간외 호가잔량 순위
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHPST01760000` |
| **메서드** | `after_hour_balance()` |
| **Endpoint** | `/uapi/domestic-stock/v1/ranking/after-hour-balance` |
| **HTTP** | GET |
| **용도** | 시간외 시세 잔량 상위 종목 순위 |

#### 6.4 호가잔량 순위
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHPST01720000` |
| **메서드** | `quote_balance()` |
| **Endpoint** | `/uapi/domestic-stock/v1/ranking/quote-balance` |
| **HTTP** | GET |
| **용도** | 매수/매도 호가 잔량 상위 종목 |

---

### 7. 투자의견 API

#### 7.1 증권사별 투자의견
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST663400C0` |
| **메서드** | `invest_opbysec()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/invest-opbysec` |
| **HTTP** | GET |
| **용도** | 증권사별 투자 의견 수집 |

#### 7.2 종목 투자의견
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST663300C0` |
| **메서드** | `invest_opinion()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/invest-opinion` |
| **HTTP** | GET |
| **용도** | 특정 종목의 투자 의견 |

---

### 8. 거래량/매매동향 API

#### 8.1 종목별 일별 매수매도 체결량
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST03010800` |
| **메서드** | `inquire_daily_trade_volume()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/inquire-daily-trade-volume` |
| **HTTP** | GET |
| **용도** | 외국인/기관의 매도/매수 거래량 |

#### 8.2 기관/외국인 매매종목가 집계
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHPTJ04400000` |
| **메서드** | `foreign_institution_total()` |
| **Endpoint** | `/uapi/domestic-stock/v1/quotations/foreign-institution-total` |
| **HTTP** | GET |
| **용도** | 기관/외국인의 매매금액 집계 |

---

### 9. 재무정보 API

#### 9.1 대차대조표
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430100` |
| **메서드** | `balance_sheet()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/balance-sheet` |
| **HTTP** | GET |
| **용도** | 기업 재무제표 - 자산, 부채, 자본 |

#### 9.2 손익계산서
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430200` |
| **메서드** | `income_statement()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/income-statement` |
| **HTTP** | GET |
| **용도** | 기업 재무제표 - 수익, 비용, 이익 |

#### 9.3 재무비율
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430300` |
| **메서드** | `financial_ratio()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/financial-ratio` |
| **HTTP** | GET |
| **용도** | PER, PBR, ROE, ROA 등 재무비율 |

#### 9.4 수익성비율
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430400` |
| **메서드** | `profit_ratio()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/profit-ratio` |
| **HTTP** | GET |
| **용도** | 순이익률, 영업이익률 등 |

#### 9.5 기타주요비율
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430500` |
| **메서드** | `other_major_ratios()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/other-major-ratios` |
| **HTTP** | GET |
| **용도** | 배당수익률, 부채비율 등 |

#### 9.6 안정성비율
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430600` |
| **메서드** | `stability_ratio()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/stability-ratio` |
| **HTTP** | GET |
| **용도** | 유동비율, 당좌비율, 차입금비율 등 |

#### 9.7 성장성비율
| 항목 | 내용 |
|------|------|
| **TR CD** | `FHKST66430600` |
| **메서드** | `growth_ratio()` |
| **Endpoint** | `/uapi/domestic-stock/v1/finance/growth-ratio` |
| **HTTP** | GET |
| **용도** | 매출증가율, 순이익증가율 등 |

---

### 10. 인증 API

#### 10.1 접근 토큰 발급
| 항목 | 내용 |
|------|------|
| **메서드** | `set_access_token_from_kis()` |
| **Endpoint** | `/oauth2/tokenP` 또는 `/oauth2/Approval` |
| **HTTP** | POST |
| **용도** | Bearer 토큰 발급 및 갱신 |
| **유효기간** | 23시간 (공식 24시간) |
| **요청** | `grant_type`: "client_credentials", `appkey`, `secretkey` |

#### 10.2 Hash Key 생성
| 항목 | 내용 |
|------|------|
| **메서드** | `hashkey()` |
| **Endpoint** | `/uapi/hashkey` |
| **HTTP** | POST |
| **용도** | POST 요청 검증용 암호화 해시키 생성 |

---

## WebSocket API (실시간 데이터)

### 연결 정보

| 항목 | 내용 |
|------|------|
| **서버** | `ws://ops.koreainvestment.com:21000` |
| **인증** | `approval_key` + `personalseckey` |
| **암호화** | AES-256-CBC (Base64) |

### 실시간 TR ID 목록

| TR ID | 이름 | 용도 | 구독 |
|-------|------|------|------|
| `H0STASP0` | 실시간 호가 | 호가(bid/ask) 실시간 갱신 | TR Type "1" |
| `H0STCNT0` | 실시간 체결 | 거래 체결 정보 실시간 전송 | TR Type "1" |
| `H0STCNI0` | 계좌체결 통보 | 계좌 내 주문 체결 통보 | TR Type "1" |

### 구독/구독해제

```python
# 구독
subscribe(tr_id, stock_code)  # TR Type: "1"

# 구독해제
unsubscribe(tr_id, stock_code)  # TR Type: "2"
```

### WebSocket 메시지 흐름

```
1. 초기화 → APP_KEY, APP_SECRET, HTS_USER_ID 로드
2. 연결 → ws://ops.koreainvestment.com:21000
3. 개방 → H0STCNI0(체결통보) 자동 구독, AES Key 수신
4. 데이터 수신:
   - PINGPONG → pong 응답
   - 암호화 데이터 → AES-CBC 복호화
   - 클라이언트로 브로드캐스트
5. 연결 해제
```

---

## API 요약

| 분류 | 개수 | 주요 API |
|------|------|----------|
| 시세조회 | 5개 | 현재가, 분봉, 일봉 |
| 주문 | 3개 | 매수/매도, 취소, 정정 |
| 잔고/계좌 | 6개 | 잔고, 체결, 주문가능수량 |
| 조건식 | 2개 | 목록, 결과 |
| 관심종목 | 3개 | 그룹, 종목, 멀티시세 |
| 종목/시장정보 | 4개 | 종목검색, 휴장일, 호가순위 |
| 투자의견 | 2개 | 증권사별, 종목별 |
| 거래량 | 2개 | 일별체결량, 기관외국인 |
| 재무정보 | 7개 | 재무제표, 재무비율 |
| 인증 | 2개 | 토큰발급, 해시키 |
| WebSocket | 3개 | 호가, 체결, 계좌통보 |
| **총합** | **39개** | - |

---

## 주요 코드/제약사항

### 주문구분 코드 (ORD_DVSN)
| 코드 | 설명 |
|------|------|
| 00 | 지정가 |
| 01 | 시장가 |
| 02 | 조건부지정가 |
| 03 | 최유리지정가 |
| 04 | 최우선지정가 |

### 매도/매수 구분 (SLL_BUY_DVSN_CD)
| 코드 | 설명 |
|------|------|
| 00 | 전체 |
| 01 | 매도 |
| 02 | 매수 |

### 토큰 관련
- **유효기간**: 23시간 (실제 24시간이나 보수적으로 체크)
- **갱신 제한**: 1분에 1회
- **만료 에러**: `rt_cd=1, msg_cd=EGW00123`
- **무효 토큰**: `rt_cd=1, msg_cd=EGW00121`

### 계좌번호 파싱
- **형식**: 10자리 (8자리 계좌 + 2자리 상품코드)
- **CANO**: `ACCTNO[0:8]` (앞 8자리)
- **ACNT_PRDT_CD**: `ACCTNO[8:10]` (뒤 2자리)

import yfinance as yf

# 나스닥 지수 가져오기
nasdaq = yf.Ticker("^IXIC")
print(nasdaq.history(period="1d"))

# 금 선물 시세 가져오기
gold = yf.Ticker("GC=F")
print(gold.history(period="1d"))

# 환율 (원/달러) 가져오기
usd_krw = yf.Ticker("USDKRW=X")
print(usd_krw.history(period="1d"))
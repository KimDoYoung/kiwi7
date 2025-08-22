-- settings table 실상은 name value
CREATE TABLE IF NOT EXISTS settings (
    name TEXT PRIMARY KEY,
    value TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT OR IGNORE INTO settings (name, value) VALUES ('user_id', 'kdy987');
INSERT OR IGNORE INTO settings (name, value) VALUES ('user_pw', '1111');

-- kdemon_rules: 자동매매 룰
CREATE TABLE IF NOT EXISTS kdemon_rules (
  id                INTEGER PRIMARY KEY AUTOINCREMENT,
  name              TEXT NOT NULL,
  symbol            TEXT NOT NULL,                -- 종목코드 (예: 005930)
  condition_op      TEXT NOT NULL,                -- 'gte' | 'lte' | 'cross_up' | 'cross_down'
  threshold         REAL NOT NULL,                -- 기준값 (예: 100.0)
  action            TEXT NOT NULL,                -- 'buy' | 'sell'
  qty               INTEGER NOT NULL,             -- 수량
  status            TEXT NOT NULL DEFAULT 'active', -- 'active' | 'paused' | 'done'
  cooldown_sec      INTEGER NOT NULL DEFAULT 60,  -- 재트리거 쿨다운
  valid_from        TEXT,                         -- 'YYYYMMDDHHMMSS' (옵션)
  valid_to          TEXT,                         -- 'YYYYMMDDHHMMSS' (옵션)
  last_price        REAL,                         -- 직전 가격(크로스 판정용)
  last_triggered_at TEXT,                         -- 마지막 실행 시각 'YYYYMMDDHHMMSS'
  notes             TEXT,
  created_at       TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- kdemon_commands: 제어 명령 큐
CREATE TABLE IF NOT EXISTS kdemon_commands (
  id           INTEGER PRIMARY KEY AUTOINCREMENT,
  cmd          TEXT NOT NULL,            -- 'start' | 'stop' | 'refresh'
  args_json    TEXT,                     -- 옵션 인자(JSON)
  created_at   TEXT NOT NULL,            -- 'YYYYMMDDHHMMSS'
  processed_at TEXT                      -- 처리 완료 시각
);

-- kdemon_state: 데몬 상태(싱글톤 1row)
CREATE TABLE IF NOT EXISTS kdemon_state (
  id             INTEGER PRIMARY KEY CHECK (id = 1),
  status         TEXT NOT NULL,  -- 'stopped' | 'running'
  updated_at     TEXT NOT NULL
);

-- ---------------------------------------------------------------
-- my_stock
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS my_stock (
  stk_cd     TEXT    NOT NULL,                               -- 종목코드 (PK)
  stk_nm     TEXT    NOT NULL,                               -- 종목명
  sector     TEXT    NULL,                                   -- 분야
  is_hold    INTEGER NOT NULL DEFAULT 0                      -- 보유여부 (0/1)
             CHECK (is_hold IN (0,1)),
  is_watch   INTEGER NOT NULL DEFAULT 0                      -- 관심여부 (0/1)
             CHECK (is_watch IN (0,1)),
  note       TEXT,                                           -- 메모
  created_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now','localtime')),
  updated_at TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%d %H:%M:%S','now','localtime')),
  PRIMARY KEY (stk_cd)
);
-- ---------------------------------------------------------------
-- stk_diary : 주식에 대한 생각을 기록, 종목토론
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS stk_diary (
    id        INTEGER PRIMARY KEY AUTOINCREMENT,  -- 고유 ID
    ymd       TEXT NOT NULL,                     -- 날짜 (YYYYMMDD)
    stk_cd    TEXT NULL,                     -- 종목코드 (FK)
    note      TEXT NOT NULL,                     -- 일지 내용
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 생성 시각
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 수정 시각
);

-- ---------------------------------------------------------------
-- stk_trades_history : 특정종목에 대한 매매 기록
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS stk_trades_history (
  id        INTEGER PRIMARY KEY AUTOINCREMENT,  -- 고유 ID
  stk_cd    TEXT    NOT NULL,                     -- 종목코드 (FK)
  stk_nm    TEXT    NOT NULL,                     -- 종목명
  ymd       TEXT    NOT NULL,                     -- 거래일 (YYYYMMDD)     
  note      TEXT    NOT NULL,                      -- 메모
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, -- 생성 시각
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP -- 수정 시각
);
-- ---------------------------------------------------------------
-- stk_cache : 전일종가와 같은 종목에 대한 일시적인 값 기록
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS stk_cache (
  id         INTEGER PRIMARY KEY AUTOINCREMENT,    -- 고유 ID
  stk_cd     TEXT    NOT NULL,                     -- 종목코드
  name       TEXT    NOT NULL,                     -- 종목명
  value      TEXT    NOT NULL,                     -- 전일종가 등 값
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   -- 생성 시각
);
-- ---------------------------------------------------------------
-- 종목 기본정보 국내주식 > 종목정보 > 종목정보 리스트(ka10099) 결과를 넣어두기 위함
-- ---------------------------------------------------------------
CREATE TABLE IF NOT EXISTS stk_info (
  code                TEXT PRIMARY KEY,                                      -- 종목코드(단축코드)
  name                TEXT,                                                  -- 종목명
  list_count          TEXT,                                                  -- 상장주식수 (API 원문: String)
  audit_info          TEXT,                                                  -- 감리구분
  reg_day             TEXT,                                                  -- 상장일 (YYYYMMDD)
  last_price          TEXT,                                                  -- 전일종가
  state               TEXT,                                                  -- 종목상태
  market_code         TEXT,                                                  -- 시장구분코드
  market_name         TEXT,                                                  -- 시장명
  up_name             TEXT,                                                  -- 업종명
  up_size_name        TEXT,                                                  -- 회사크기분류
  company_class_name  TEXT,                                                  -- 회사분류 (코스닥만 존재)
  order_warning       TEXT CHECK (order_warning IN ('0','1','2','3','4','5')), 
  -- 투자유의종목여부: 0 해당없음, 2 정리매매, 3 단기과열, 4 투자위험, 5 투자경과, 1 ETF투자주의요망
  nxt_enable          TEXT CHECK (nxt_enable IN ('Y','N')),                  -- NXT 가능여부 (Y/N)
  created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP                    -- 생성 시각
);
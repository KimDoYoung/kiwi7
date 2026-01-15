# Kiwi7 개발 도구 모음

프로젝트 개발/운영에 유용한 스크립트 모음

## 📁 구조

```
tools/
├── README.md           # 이 파일
├── db/                 # 데이터베이스 관련 도구
├── token/              # 토큰 관리 도구
├── logs/               # 로그 분석 도구
├── test/               # 테스트 데이터 생성
├── api/                # API 테스트 스크립트
└── setup/              # 환경 설정 도구
```

## 🛠 주요 도구

### 데이터베이스 (db/)
- `init_db.sh` - DB 초기화
- `backup_db.sh` - DB 백업
- `query_db.py` - 간단한 쿼리 실행 도구

### 토큰 관리 (token/)
- `issue_token.py` - 증권사별 토큰 발급
- `check_token.py` - 토큰 상태 확인
- `revoke_token.py` - 토큰 폐기

### 로그 분석 (logs/)
- `tail_log.sh` - 실시간 로그 모니터링
- `analyze_error.py` - 에러 로그 분석
- `log_stats.py` - 로그 통계

### 테스트 데이터 (test/)
- `create_test_data.py` - 테스트용 종목 데이터 생성
- `mock_stock_data.py` - Mock 주식 데이터

### API 테스트 (api/)
- `test_kiwoom.py` - 키움 API 테스트
- `test_kis.py` - KIS API 테스트
- `test_ls.py` - LS API 테스트

### 환경 설정 (setup/)
- `check_env.py` - 환경 변수 검증
- `setup_dev.sh` - 개발 환경 설정
- `setup_docker.sh` - Docker 환경 설정

## 📝 사용법

### 실행 권한 부여
```bash
chmod +x tools/**/*.sh
```

### Python 스크립트 실행
```bash
# 프로젝트 루트에서 실행
python -m tools.db.query_db
python -m tools.token.issue_token
```

### Shell 스크립트 실행
```bash
./tools/db/init_db.sh
./tools/logs/tail_log.sh
```

## 🔧 개발 가이드

### 새로운 도구 추가 시
1. 적절한 카테고리 폴더에 배치
2. 스크립트 상단에 사용법 주석 추가
3. README.md 업데이트
4. 실행 권한 설정 (shell script의 경우)

### 코딩 규칙
- Python: 프로젝트의 코딩 규칙 준수 (한글 주석)
- Shell: #!/bin/bash 또는 #!/usr/bin/env bash 사용
- 에러 처리 필수
- 사용 예시 포함

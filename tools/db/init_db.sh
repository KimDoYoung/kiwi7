#!/bin/bash
# DB 초기화 스크립트
# 사용법: ./tools/db/init_db.sh [환경]
# 예시: ./tools/db/init_db.sh local

set -e

ENV=${1:-local}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "========================================"
echo "Kiwi7 DB 초기화"
echo "환경: $ENV"
echo "========================================"

# .env 파일 로드
ENV_FILE="$PROJECT_ROOT/.env.$ENV"
if [ ! -f "$ENV_FILE" ]; then
    echo "❌ 에러: $ENV_FILE 파일이 없습니다."
    exit 1
fi

# BASE_DIR 추출
BASE_DIR=$(grep "^BASE_DIR=" "$ENV_FILE" | cut -d '=' -f2)
DB_PATH="$BASE_DIR/db/kiwi7.db"

echo "📁 DB 경로: $DB_PATH"

# 기존 DB 백업
if [ -f "$DB_PATH" ]; then
    BACKUP_PATH="${DB_PATH}.backup.$(date +%Y%m%d_%H%M%S)"
    echo "💾 기존 DB 백업: $BACKUP_PATH"
    cp "$DB_PATH" "$BACKUP_PATH"
    rm "$DB_PATH"
fi

# DB 디렉토리 생성
mkdir -p "$(dirname "$DB_PATH")"

# DDL 실행
DDL_FILE="$PROJECT_ROOT/sqls/kiwi7_ddl.sql"
if [ ! -f "$DDL_FILE" ]; then
    echo "❌ 에러: DDL 파일이 없습니다: $DDL_FILE"
    exit 1
fi

echo "🔧 DDL 실행 중..."
sqlite3 "$DB_PATH" < "$DDL_FILE"

# 테이블 확인
echo ""
echo "✅ 생성된 테이블:"
sqlite3 "$DB_PATH" "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name;"

echo ""
echo "✅ DB 초기화 완료!"

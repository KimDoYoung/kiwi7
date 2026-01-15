#!/bin/bash
# DB 백업 스크립트
# 사용법: ./tools/db/backup_db.sh [환경] [백업디렉토리]
# 예시: ./tools/db/backup_db.sh local ~/backup

set -e

ENV=${1:-local}
BACKUP_DIR=${2:-~/backup/kiwi7}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

echo "========================================"
echo "Kiwi7 DB 백업"
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

if [ ! -f "$DB_PATH" ]; then
    echo "❌ 에러: DB 파일이 없습니다: $DB_PATH"
    exit 1
fi

# 백업 디렉토리 생성
mkdir -p "$BACKUP_DIR"

# 백업 파일명 (날짜_시간 포함)
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/kiwi7_${ENV}_${TIMESTAMP}.db"

# 백업 실행
echo "💾 백업 중: $DB_PATH → $BACKUP_FILE"
cp "$DB_PATH" "$BACKUP_FILE"

# 압축
echo "🗜️  압축 중..."
gzip "$BACKUP_FILE"
BACKUP_FILE="${BACKUP_FILE}.gz"

# 파일 크기 확인
SIZE=$(du -h "$BACKUP_FILE" | cut -f1)

echo ""
echo "✅ 백업 완료!"
echo "📦 백업 파일: $BACKUP_FILE"
echo "📊 파일 크기: $SIZE"

# 오래된 백업 삭제 (7일 이상)
echo ""
echo "🧹 오래된 백업 파일 정리 (7일 이상)..."
find "$BACKUP_DIR" -name "kiwi7_*.db.gz" -mtime +7 -delete
echo "✅ 정리 완료!"

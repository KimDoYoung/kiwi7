#!/bin/bash
# 실시간 로그 모니터링 스크립트
# 사용법: ./tools/logs/tail_log.sh [환경] [라인수]
# 예시: ./tools/logs/tail_log.sh local 100

set -e

ENV=${1:-local}
LINES=${2:-50}
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"

# .env 파일 로드
ENV_FILE="$PROJECT_ROOT/.env.$ENV"
if [ ! -f "$ENV_FILE" ]; then
    echo "❌ 에러: $ENV_FILE 파일이 없습니다."
    exit 1
fi

# BASE_DIR 추출
BASE_DIR=$(grep "^BASE_DIR=" "$ENV_FILE" | cut -d '=' -f2)
# ~를 홈 디렉토리로 확장
BASE_DIR="${BASE_DIR/#\~/$HOME}"
LOG_FILE="$BASE_DIR/logs/kiwi7.log"

echo "========================================"
echo "Kiwi7 로그 모니터링"
echo "환경: $ENV"
echo "로그 파일: $LOG_FILE"
echo "========================================"
echo ""

if [ ! -f "$LOG_FILE" ]; then
    echo "❌ 로그 파일이 없습니다: $LOG_FILE"
    exit 1
fi

# tail -f로 실시간 모니터링
tail -n "$LINES" -f "$LOG_FILE"

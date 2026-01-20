"""
settings 테이블의 토큰 데이터를 tokens 테이블로 마이그레이션
"""
import sqlite3
import sys
from pathlib import Path

# 프로젝트 루트를 sys.path에 추가
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from backend.core.config import config
from backend.core.logger import get_logger

logger = get_logger(__name__)


def migrate_tokens():
    """settings → tokens 마이그레이션"""
    db_path = config.DB_PATH
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    try:
        # 1. Kiwoom 토큰 마이그레이션
        logger.info('Kiwoom 토큰 마이그레이션 시작...')
        cur.execute('SELECT value FROM settings WHERE name = ?', ('ACCESS_TOKEN',))
        kiwoom_token_row = cur.fetchone()

        cur.execute(
            'SELECT value FROM settings WHERE name = ?',
            ('ACCESS_TOKEN_EXPIRED_TIME',),
        )
        kiwoom_expires_row = cur.fetchone()

        if kiwoom_token_row and kiwoom_expires_row:
            cur.execute(
                'INSERT OR REPLACE INTO tokens (broker_type, access_token, expires_at) VALUES (?, ?, ?)',
                ('KIWOOM', kiwoom_token_row[0], kiwoom_expires_row[0]),
            )
            logger.info('✓ Kiwoom 토큰 마이그레이션 완료')
        else:
            logger.info('- Kiwoom 토큰 없음 (스킵)')

        # 2. KIS 토큰 마이그레이션
        logger.info('KIS 토큰 마이그레이션 시작...')
        cur.execute(
            'SELECT value FROM settings WHERE name = ?', ('KIS_ACCESS_TOKEN',)
        )
        kis_token_row = cur.fetchone()

        cur.execute(
            'SELECT value FROM settings WHERE name = ?',
            ('KIS_ACCESS_TOKEN_EXPIRED_TIME',),
        )
        kis_expires_row = cur.fetchone()

        if kis_token_row and kis_expires_row:
            cur.execute(
                'INSERT OR REPLACE INTO tokens (broker_type, access_token, expires_at) VALUES (?, ?, ?)',
                ('KIS', kis_token_row[0], kis_expires_row[0]),
            )
            logger.info('✓ KIS 토큰 마이그레이션 완료')
        else:
            logger.info('- KIS 토큰 없음 (스킵)')

        # 3. LS 토큰 마이그레이션
        logger.info('LS 토큰 마이그레이션 시작...')
        cur.execute(
            'SELECT value FROM settings WHERE name = ?', ('LS_ACCESS_TOKEN',)
        )
        ls_token_row = cur.fetchone()

        cur.execute(
            'SELECT value FROM settings WHERE name = ?',
            ('LS_ACCESS_TOKEN_EXPIRED_TIME',),
        )
        ls_expires_row = cur.fetchone()

        if ls_token_row and ls_expires_row:
            cur.execute(
                'INSERT OR REPLACE INTO tokens (broker_type, access_token, expires_at) VALUES (?, ?, ?)',
                ('LS', ls_token_row[0], ls_expires_row[0]),
            )
            logger.info('✓ LS 토큰 마이그레이션 완료')
        else:
            logger.info('- LS 토큰 없음 (스킵)')

        conn.commit()

        # 4. 마이그레이션 결과 확인
        logger.info('\n=== 마이그레이션 결과 ===')
        cur.execute('SELECT broker_type, expires_at FROM tokens')
        for row in cur.fetchall():
            logger.info(f'  {row[0]}: 만료시각 {row[1]}')

        logger.info('\n마이그레이션 완료!')
        logger.info(
            '주의: settings 테이블의 토큰 데이터는 아직 삭제되지 않았습니다.'
        )
        logger.info(
            '      tokens 테이블 사용이 안정화된 후 수동으로 삭제하세요.'
        )

    except Exception as e:
        logger.error(f'마이그레이션 실패: {e}')
        conn.rollback()
        raise
    finally:
        conn.close()


if __name__ == '__main__':
    migrate_tokens()

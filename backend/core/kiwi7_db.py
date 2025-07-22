def create_kiwi7_db(db_path: str):
    """
    Kiwi7 데이터베이스를 생성하는 함수
    :param db_path: 데이터베이스 파일 경로
    """
    import sqlite3

    # SQLite 데이터베이스 연결
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # 필요한 테이블 생성 (예시로 users 테이블 생성)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT PRIMARY KEY,
            value TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    # insert name kdy987, value 1111 if not exists
    cursor.execute('''
        INSERT OR IGNORE INTO users (name, value) VALUES (?, ?)
    ''', ('user_id', 'kdy987'))
    cursor.execute('''
        INSERT OR IGNORE INTO users (name, value) VALUES (?, ?)
    ''', ('user_pw', '1111'))


    # 변경사항 저장 및 연결 종료
    conn.commit()
    conn.close()
#!/usr/bin/env python3
"""
간단한 DB 쿼리 실행 도구

사용법:
    python -m tools.db.query_db "SELECT * FROM settings"
    python -m tools.db.query_db --table my_stock
    python -m tools.db.query_db --tables  # 모든 테이블 목록
"""
import os
import sys
import sqlite3
import argparse
from pathlib import Path
from tabulate import tabulate

# 프로젝트 루트를 path에 추가
project_root = Path(__file__).parent.parent.parent
sys.path.insert(0, str(project_root))

from backend.core.config import config


def get_db_path():
    """DB 경로 가져오기"""
    return config.DB_PATH


def execute_query(query: str):
    """쿼리 실행 및 결과 출력"""
    db_path = get_db_path()
    
    if not os.path.exists(db_path):
        print(f"❌ DB 파일이 없습니다: {db_path}")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    try:
        cursor.execute(query)
        
        # SELECT 쿼리인 경우
        if query.strip().upper().startswith('SELECT'):
            rows = cursor.fetchall()
            if rows:
                # 컬럼명 가져오기
                columns = [description[0] for description in cursor.description]
                # 테이블 형식으로 출력
                print(tabulate(rows, headers=columns, tablefmt='grid'))
                print(f"\n총 {len(rows)}개 행")
            else:
                print("결과가 없습니다.")
        else:
            # INSERT, UPDATE, DELETE 등
            conn.commit()
            print(f"✅ 쿼리 실행 완료. 영향받은 행: {cursor.rowcount}")
            
    except sqlite3.Error as e:
        print(f"❌ 쿼리 실행 오류: {e}")
    finally:
        conn.close()


def list_tables():
    """모든 테이블 목록 출력"""
    query = "SELECT name FROM sqlite_master WHERE type='table' ORDER BY name"
    execute_query(query)


def show_table(table_name: str):
    """특정 테이블의 모든 데이터 출력"""
    query = f"SELECT * FROM {table_name}"
    execute_query(query)


def main():
    parser = argparse.ArgumentParser(description='Kiwi7 DB 쿼리 도구')
    parser.add_argument('query', nargs='?', help='실행할 SQL 쿼리')
    parser.add_argument('--tables', action='store_true', help='모든 테이블 목록')
    parser.add_argument('--table', help='특정 테이블의 모든 데이터 조회')
    
    args = parser.parse_args()
    
    print(f"📁 DB 경로: {get_db_path()}\n")
    
    if args.tables:
        list_tables()
    elif args.table:
        show_table(args.table)
    elif args.query:
        execute_query(args.query)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()

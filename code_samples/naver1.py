from backend.utils.naver_utils import get_jisu_from_naver

def main():
    # 프로그램의 기본 실행 구조
    jisu = get_jisu_from_naver()
    print("주식 정보:", jisu)


if __name__ == "__main__":
    main()
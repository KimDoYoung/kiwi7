# naver_util.py
"""
모듈 설명: 
    - 네이버증권에서 정보를 가져온다.
주요 기능:
    -   기능을 넣으시오

작성자: 김도영
작성일: 07
버전: 1.0
"""

from bs4 import BeautifulSoup
import requests
def get_name_by_code(code: str):
    '''주식 코드로부터 주식 이름을 가져온다.'''
    stock_info = get_stock_info(code)
    if stock_info['stk_name'] is not None:
        return stock_info['stk_name']
    else:
        return None

def extract_index_data(soup,area_selector):
    """각 영역(KOSPI, KOSDAQ, KOSPI200)에서 지수, 전일대비, 등락률을 추출"""
    area = soup.select_one(area_selector)
    if not area:
        return None
    
    nums = area.select_one(".num_quot").find_all("span", class_=["num", "num2", "num3"])
    
    index_value = nums[0].get_text(strip=True)  # 지수
    diff = nums[1].get_text(strip=True)         # 전일대비
    change_rate = nums[2].get_text(strip=True).replace("퍼센트", "").replace("%", "")  # 등락률
    
    return {
        "index": index_value,
        "diff": diff,
        "rate": change_rate
    }

def get_jisu_from_naver():
    '''네이버에서 지수를 가져온다.'''
    page = requests.get("https://finance.naver.com/")
    soup = BeautifulSoup(page.text, 'html.parser')
    kospi_data = extract_index_data(soup, ".kospi_area")
    kosdaq_data = extract_index_data(soup, ".kosdaq_area")
    kospi_200 = extract_index_data(soup, ".kospi200_area")
    return {
        "KOSPI": kospi_data,
        "KOSDAQ": kosdaq_data,
        "KOSPI200": kospi_200
    }

def get_summary_from_naver(stk_code: str):
    '''주식 코드로부터 주식 요약 정보를 가져온다.'''
    page = requests.get(f"https://finance.naver.com/item/main.nhn?code={stk_code}")
    soup = BeautifulSoup(page.text, 'html.parser')
    div_class_name = 'wrap_company'
    stk_name = soup.select_one(f'div.{div_class_name} h2 a').text

    # 기업개요: summary_info 클래스 내부의 모든 <p> 태그를 찾음
    summary_info = soup.find('div', class_='summary_info')
    paragraphs = summary_info.find_all('p')
    
    # <p> 태그 내용을 줄바꿈과 함께 합침
    company_summary = "\n".join(p.get_text(strip=True) for p in paragraphs)
    return company_summary


def get_stock_info(stk_code: str):
    '''주식 코드로부터 주식 정보를 가져온다.'''
    page = requests.get(f"https://finance.naver.com/item/main.nhn?code={stk_code}")
    soup = BeautifulSoup(page.text, 'html.parser')
    div_class_name = 'wrap_company'
    stk_name = soup.select_one(f'div.{div_class_name} h2 a').text

    # 기업개요: summary_info 클래스 내부의 모든 <p> 태그를 찾음
    summary_info = soup.find('div', class_='summary_info')
    paragraphs = summary_info.find_all('p')
    
    # <p> 태그 내용을 줄바꿈과 함께 합침
    company_summary = "\n".join(p.get_text(strip=True) for p in paragraphs)

    # 필요한 div 컨테이너를 먼저 찾아서 그 안에서 작업
    container_div = soup.find('div', id='tab_con1', class_='tab_con1')
    
    # 시가총액
    market_cap = container_div.find('th', string='시가총액').find_next('td').get_text(separator='').strip()

    # 시가총액순위
    market_cap_rank = container_div.find('a', string='시가총액순위').find_next('td').get_text(separator='').strip()

    # 상장주식수
    num_of_shares = container_div.find('th', string='상장주식수').find_next('td').get_text(separator='').strip()


    # # 1. pArea 영역을 먼저 찾기
    # pArea = soup.find('div', id='pArea')

    # # 2. pArea 내부에서 class="cmp-table-cell td0301"을 찾기
    # table_cell = pArea.find('td', class_='cmp-table-cell td0301')

    # # 3. EPS, BPS, PER, 업종PER, PBR, 현금배당수익률을 추출
    # eps = table_cell.find('dt', string='EPS ').find('b', class_='num').text
    # bps = table_cell.find('dt', string='BPS ').find('b', class_='num').text
    # per = table_cell.find('dt', string='PER ').find('b', class_='num').text
    # sector_per = table_cell.find('dt', string='업종PER ').find('b', class_='num').text
    # pbr = table_cell.find('dt', string='PBR ').find('b', class_='num').text
    # div_yield = table_cell.find('dt', string='현금배당수익률 ').find('b', class_='num').text

    stock_info = {
        'stk_code': stk_code,
        'stk_name': stk_name,
        'company_summary': company_summary,
        'market_cap': market_cap,
        'market_cap_rank': market_cap_rank,
        'num_of_shares': num_of_shares,
        # 'EPS': eps,
        # 'BPS': bps,
        # 'PER': per,
        # '업종PER': sector_per,
        # 'PBR': pbr,
        # '현금배당수익률': div_yield
    }
    return stock_info
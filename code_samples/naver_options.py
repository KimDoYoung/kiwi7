import requests
from bs4 import BeautifulSoup
import time
import json

# 네이버 종목토론방 capture
def capture_naver_forum(stock_code):
    """
    네이버 종목토론방에서 게시물 정보를 수집
    Args:
        stock_code: 종목코드
    Returns:
        list: 각 게시물의 날짜, 제목, href를 포함한 딕셔너리 리스트
    """
    page_no_list = [1, 2]
    posts_list = []
    
    # 각 페이지를 순회하면서 게시물 수집
    for page_no in page_no_list:
        page_posts = get_lists(stock_code, page_no)
        posts_list.extend(page_posts)
        print(f"{page_no}페이지에서 {len(page_posts)}개 게시물 수집")
    
    print(f"전체 수집된 게시물: {len(posts_list)}개")
    return posts_list


def get_lists(stk_code, page_no):
    """
    종목토론방 페이지에서 게시물 정보를 추출
    Args:
        stk_code: 종목코드
        page_no: 페이지 번호
    Returns:
        list: 게시물 정보 리스트 [{'date': '날짜', 'title': '제목', 'href': '링크'}, ...]
    """
    url = f"https://finance.naver.com/item/board.naver?code={stk_code}&page={page_no}"
    
    # 브라우저와 유사한 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://finance.naver.com/'
    }
    
    # 세션 사용으로 쿠키 유지
    session = requests.Session()
    session.headers.update(headers)
    
    try:
        # 요청 간격 조절 (너무 빠른 요청 방지)
        time.sleep(1)
        
        response = session.get(url, timeout=10)
        response.raise_for_status()
        
        print(f"페이지 {page_no} - 응답 상태 코드: {response.status_code}")
        print(f"페이지 {page_no} - 응답 크기: {len(response.text)} bytes")
        
    except requests.exceptions.RequestException as e:
        print(f"페이지 {page_no} 요청 중 오류 발생: {e}")
        return []
    
    soup = BeautifulSoup(response.text, "html.parser")
    
    # class명이 'type2'인 테이블 찾기
    table = soup.find('table', class_='type2')
    
    if not table:
        print(f"페이지 {page_no}에서 type2 클래스를 가진 테이블을 찾을 수 없습니다.")
        # 다른 가능한 테이블 클래스명들 확인
        all_tables = soup.find_all('table')
        print(f"페이지 {page_no} - 전체 테이블 개수: {len(all_tables)}")
        for i, tbl in enumerate(all_tables):
            print(f"페이지 {page_no} - 테이블 {i+1}: {tbl.get('class', '클래스 없음')}")
        return []
    
    posts_list = []
    
    # onMouseOver 속성이 있는 tr 태그들만 찾기
    rows = table.find_all('tr', onmouseover=True)
    print(f"페이지 {page_no} - onMouseOver가 있는 행 개수: {len(rows)}")
    
    for idx, row in enumerate(rows):
        # 각 행에서 td 태그들 찾기
        tds = row.find_all('td')
        
        if len(tds) >= 3:  # 충분한 컬럼이 있는지 확인
            try:
                # 첫 번째 td에서 날짜 추출
                date_span = tds[0].find('span', class_='tah p10 gray03')
                date = date_span.get_text(strip=True) if date_span else ''
                
                # 두 번째 td(class='title')에서 제목과 href 추출
                title_td = tds[1]
                if title_td and 'title' in title_td.get('class', []):
                    anchor = title_td.find('a', title=True)
                    if anchor:
                        title = anchor.get('title', '').strip()
                        href = anchor.get('href', '').strip()
                        
                        # 유효한 데이터가 있을 때만 추가
                        if date and title and href:
                            posts_list.append({
                                'date': date,
                                'title': title,
                                'href': href,
                                'page': page_no  # 어느 페이지에서 가져온 것인지 표시
                            })
                            
            except Exception as e:
                # 파싱 에러 발생 시 해당 행은 건너뛰기
                print(f"페이지 {page_no} - 행 {idx+1} 파싱 오류: {e}")
                continue
    
    print(f"페이지 {page_no}에서 {len(posts_list)}개 게시물 추출 완료")
    return posts_list


def detail_collect(posts_list):
    """
    게시물 목록을 순회하며 각 게시물의 상세 내용을 추출
    Args:
        posts_list: 게시물 정보 리스트
    """
    # 브라우저와 유사한 헤더 설정
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Language': 'ko-KR,ko;q=0.9,en;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'Referer': 'https://finance.naver.com/'
    }
    
    # 세션 사용으로 쿠키 유지
    session = requests.Session()
    session.headers.update(headers)
    
    for idx, post in enumerate(posts_list):
        print(f"\n{'='*60}")
        print(f"게시물 {idx+1}: {post['title']}")
        print(f"날짜: {post['date']}")
        print(f"{'='*60}")
        
        try:
            # 게시물 상세 페이지 URL 생성 (상대경로를 절대경로로 변환)
            if post['href'].startswith('/'):
                detail_url = f"https://finance.naver.com{post['href']}"
            else:
                detail_url = post['href']
            
            print(f"상세 URL: {detail_url}")
            
            # 요청 간격 조절
            time.sleep(1)
            
            # 게시물 상세 페이지 요청
            response = session.get(detail_url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, "html.parser")
            
            # 'view' 클래스를 갖는 테이블 찾기
            view_table = soup.find('table', class_='view')
            
            if not view_table:
                print("view 클래스를 가진 테이블을 찾을 수 없습니다.")
                continue
            
            # 테이블 내에서 iframe 찾기
            iframe = view_table.find('iframe')
            
            if not iframe:
                print("iframe을 찾을 수 없습니다.")
                continue
            
            # iframe의 src 속성 추출
            iframe_src = iframe.get('src')
            
            if not iframe_src:
                print("iframe의 src 속성을 찾을 수 없습니다.")
                continue
            
            # iframe URL이 상대경로인 경우 절대경로로 변환
            iframe_url = iframe_src
            
            print(f"iframe URL: {iframe_url}")
            
            # iframe 요청을 위한 특별한 헤더 설정 (Referer를 상세 페이지로 설정)
            iframe_headers = headers.copy()
            iframe_headers['Referer'] = detail_url
            iframe_headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
            iframe_headers['X-Requested-With'] = 'XMLHttpRequest'  # AJAX 요청으로 위장
            
            # 요청 간격 조절
            time.sleep(1)
            
            # iframe 내용 요청 (새로운 헤더 사용)
            iframe_response = session.get(iframe_url, headers=iframe_headers, timeout=10)
            iframe_response.raise_for_status()
            
            print(f"iframe 응답 상태 코드: {iframe_response.status_code}")
            print(f"iframe 응답 크기: {len(iframe_response.text)} bytes")
            
            # 디버깅을 위해 iframe 내용을 파일로 저장
            with open(f"iframe_debug_{idx+1}.html", "w", encoding="utf-8") as f:
                f.write(iframe_response.text)
            print(f"디버깅용 파일 저장: iframe_debug_{idx+1}.html")
            
            iframe_soup = BeautifulSoup(iframe_response.text, "html.parser")
            
            # Next.js 앱의 __NEXT_DATA__에서 실제 콘텐츠 추출
            next_data_script = iframe_soup.find('script', {'id': '__NEXT_DATA__'})
            
            if next_data_script:
                try:
                    # JSON 데이터 파싱
                    json_data = json.loads(next_data_script.string)
                    
                    # 게시물 데이터 찾기
                    queries = json_data.get('props', {}).get('pageProps', {}).get('dehydratedState', {}).get('queries', [])
                    
                    content_html = None
                    for query in queries:
                        if 'discussion/detail' in str(query.get('queryKey', '')):
                            result = query.get('state', {}).get('data', {}).get('result', {})
                            content_html = result.get('contentHtml', '')
                            break
                    
                    if content_html:
                        print("JSON 데이터에서 contentHtml 발견!")
                        
                        # HTML 콘텐츠를 BeautifulSoup으로 파싱
                        content_soup = BeautifulSoup(content_html, "html.parser")
                        
                        # 모든 <p> 태그 찾아서 텍스트 추출
                        p_tags = content_soup.find_all('p')
                        
                        if p_tags:
                            print(f"{len(p_tags)}개의 p 태그를 찾았습니다.")
                            print("\n--- 게시물 내용 ---")
                            
                            # 각 p 태그의 텍스트를 추출하여 리스트로 저장
                            content_lines = []
                            for p_tag in p_tags:
                                # p 태그 내의 모든 텍스트 추출 (HTML 태그 제거)
                                text_content = p_tag.get_text(strip=True)
                                
                                # 빈 내용이 아닌 경우에만 추가
                                if text_content:
                                    content_lines.append(text_content)
                            
                            # 모든 텍스트를 \n으로 연결하여 출력
                            if content_lines:
                                full_content = '\n'.join(content_lines)
                                print(full_content)
                            else:
                                print("추출된 텍스트 내용이 없습니다.")
                            
                            print("\n--- 내용 끝 ---\n")
                            continue
                        else:
                            # p 태그가 없으면 전체 텍스트 추출
                            all_text = content_soup.get_text(strip=True)
                            if all_text:
                                print("\n--- 게시물 내용 (전체 텍스트) ---")
                                print(all_text)
                                print("\n--- 내용 끝 ---\n")
                                continue
                    
                except json.JSONDecodeError as e:
                    print(f"JSON 파싱 오류: {e}")
                except Exception as e:
                    print(f"JSON 데이터 처리 오류: {e}")
            
            # 기존 방식으로 p 태그 찾기 (fallback)
            p_tags = iframe_soup.find_all('p')
            
            if not p_tags:
                print("p 태그를 찾을 수 없습니다.")
                # 다른 텍스트 태그들도 확인해보기
                all_text_tags = iframe_soup.find_all(['p', 'div', 'span', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
                print(f"전체 텍스트 태그 개수: {len(all_text_tags)}")
                
                # 전체 텍스트 추출해보기
                all_text = iframe_soup.get_text(strip=True)
                if all_text:
                    print("전체 텍스트 내용 (처음 500자):")
                    print(all_text[:500])
                continue
            
            print(f"{len(p_tags)}개의 p 태그를 찾았습니다.")
            print("\n--- 게시물 내용 ---")
            
            # 각 p 태그의 텍스트를 추출하여 리스트로 저장
            content_lines = []
            for p_tag in p_tags:
                # p 태그 내의 모든 텍스트 추출 (HTML 태그 제거)
                text_content = p_tag.get_text(strip=True)
                
                # 빈 내용이 아닌 경우에만 추가
                if text_content:
                    content_lines.append(text_content)
            
            # 모든 텍스트를 \n으로 연결하여 출력
            if content_lines:
                full_content = '\n'.join(content_lines)
                print(full_content)
            else:
                print("추출된 텍스트 내용이 없습니다.")
            
            print("\n--- 내용 끝 ---\n")
            
        except requests.exceptions.RequestException as e:
            print(f"요청 중 오류 발생: {e}")
            continue
        except Exception as e:
            print(f"처리 중 오류 발생: {e}")
            continue

def main():
    """
    메인 함수 - 사용자로부터 종목코드를 입력받아 게시물 정보를 출력
    """
    stock_code = "000720"
    posts_list = capture_naver_forum(stock_code)
    
    print(f"\n총 {len(posts_list)}개의 게시물을 찾았습니다:")
    print("-" * 80)
    
    for i, post in enumerate(posts_list, 1):
        print(f"{i}. 날짜: {post['date']} (페이지: {post['page']})")
        print(f"   제목: {post['title']}")
        print(f"   링크: {post['href']}")
        print("-" * 80)
    detail_collect(posts_list)

if __name__ == "__main__":
    main()
'''
requests 라이브러리는 파이썬에서 HTTP 요청을 보내기 위해 가장 널리 사용되는 라이브러리 중 하나입니다.
사용하기 쉽고 직관적인 API를 제공하여 HTTP 요청과 응답을 쉽게 처리할 수 있습니다.
requests 라이브러리를 사용하면 GET, POST, PUT, DELETE 등 다양한 HTTP 메서드를 간편하게 사용할 수 있습니다.
'''
import requests

'''
p 315

2. 웹 크롤링의 이해
웹 크롤링(Web crawling)이란 완성된 웹 페이지에서 필요한 정보를 수집하고 선별하여 추출하는 과정을 의미.
웹 스크래핑(Web scraping)이라고 하기도 함.

    1. HTML의 개념
        HTML : Hyper Text Markup Language의 약자로 '웹 페이지를 만드는 문법을 갖춘 언어'
        HTML은 각자 역할이 정해진 태그(tag)들로 구성돼 있습니다.
    2. HTML의 구조
    html
        head
            meta
            title
        body
            h1
            div
    3. URL
        Uniform Resource Locator의 약자로 어떤 자원의 위치를 표기하는 방법을 의미함.
        https://www.google.com과 같은 인터넷 주소를 입력하는 데 이때 입력한 주소가 URL에 해당.

3. 웹 페이지 가져오기
    1. 일반 웹 페이지 정보 가져오기
'''

# url = "https://www.naver.com"
# response = requests.get(url)
# print(f"응답 코드 : {response.status_code}")
# print(response.text)
'''
        1-1. requests 모듈은 import
        1-2. 네이버의 메인 페이지 주소를 url 변수에 저장
        1-3. request 모듈의 get() 메서드를 호출하여 결과(response)를 얻어냄.
        1-4. 요청이 정상적으로 처리되었다면 응답 코들르 의미하는 status_code의 값 200이 반환
    
    2. 검색 결과 웨 페이지 정보 가져오기
        네이버에서 "파이썬"을 검색했을 때 나오는 결과 화면을 가져 오는 방법.
        이 경우 파이썬을 검색한 결과 화면의 url은
                
+---------------+----------+
| 요청 파라미터 |    값    |
+---------------+----------+
|     where     | nexearch |
|       sm      | top_hty  |
|      fbm      |    1     |
|       ie      |  utf-8   |
|     query     |  파이썬  |
+---------------+----------+

입력한 검색어 "파이썬"은 query 라는 파라미터로 전달됩니다. 그래서 나머지를 다 제거하고,
search.naver.com/search.naver?query=파이썬
이라고 입력해도 결과값은 같습니다.        
'''
# from prettytable import PrettyTable
#
# table = PrettyTable()
# table.field_names = ["요청 파라미터", "값"]
# table.add_row(["where", "nexearch"])
# table.add_row(["sm", "top_hty"])
# table.add_row(["fbm", "1"])
# table.add_row(["ie", "utf-8"])
# table.add_row(["query", "파이썬"])
#
# print(table)

# url = "https://search.naver.com/search.naver"
# param = {"query":"파이썬"}
# response = requests.get(url, params=param)
# print(response.text)
'''
requests 모듈의 get() 메서드에 params 인자에 값을 요청 파라미터 값을 저장해서 요청하고 있습니다.
요청 파라미터는 딕셔너리를 사용하면 됩니다. 만약 둘 이상의 요청 파라미터 값을 보내족자 한다면,
'''
# params = {"queary":"파이썬", "ie":"utf-8"}
# response = requests.get(url, params=param)

'''
p 321

기본 예제

네이버 웹툰 중 화요 웹툰인 '유부 감자'의 소개 페이지를 가져오는 프로그램입니다.

'''

url = "https://comic.naver.com/webtoon/list"
param = {"titleId":"822556"}
response = requests.get(url, params=param)
print(response.text)

'''
다른 웹 페이지에서 정보 가져오는 거 시킬거임
'''
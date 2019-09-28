# 설명
print("Hello Python")
print()

# 크롤러
# 웹 브라우저를 흉내내서 사람이 웹 브라우저를 통해 하는 일을 자동화하는 것
# 정보수집, 데이터 분석, 업무 자동화, 예매

# 명기법
# 1. 네이버 메인에 접속한다.
# 1) 웹 페이지에 접속해서 내용을 받아온다.
url ="https://www.naver.com/"
import requests                         # $(터미널) pip install requests
data=requests.get(url)

# 2) 내용이 잘 받아와졌는지 확인한다.
if data.status_code != requests.codes.ok:
    print("접속 실패")
    exit()

# 3) 해당 내용을 해석하기 편하게 변환한다.
from bs4 import BeautifulSoup           # $ pip install beautifulsoup4
html=BeautifulSoup(data.text, "html.parser")
#print(html)

# 2. 실시간 급등 검색어를 찾아낸다.
# 4) 변환된 내용에서 원하는 정보를 찾아낸다.
keywords=html.select(".PM_CL_realtimeKeyword_list_base .ah_a")
#html.select_one()

# 3. 화면에 출력한다.
for keyword in keywords:
    link=keyword.attrs['href']
    rank=keyword.select_one('.ah_r').text
    text=keyword.select_one('.ah_k').text
    print(rank, text, link)

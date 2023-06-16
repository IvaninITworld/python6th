from bs4 import BeautifulSoup
import requests
from datetime import datetime

# 대상의 headers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

# 접근하고자 하는 주소
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"

# headers 를 비교하고 맞다면 가져온 결과 값
response = requests.get(url,headers=headers)

# bs4 - BeautifulSoup 를 이용해서 파싱
soup = BeautifulSoup(response.text, 'html.parser')

# 랭크는 1부터
rank = 1
# span - item_title
# findAll 로 모두 찾아오기
results = soup.findAll('span','item_title')

print(response.text)

# 파일로 저장하고 쓰기
search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%Y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))

# 결과값 for 문 돌려서 랭킹만들기
for result in results:
    search_rank_file.write(str(rank)+"위:"+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1
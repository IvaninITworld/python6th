import requests
from bs4 import BeautifulSoup

url = "https://www.daum.net/"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# daum.html 파일 생성 후 파싱해온 html을 쓰기
file = open("daum.html", "w")
file.write(response.text)
file.close()
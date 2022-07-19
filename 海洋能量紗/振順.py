import requests
from bs4 import BeautifulSoup

url = 'https://www.zenshin.com.tw/tw/news/2'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find_all('div', class_='editor-row col-12')
for i in sb:
    print(i.text, end="")
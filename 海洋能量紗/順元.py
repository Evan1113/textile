import requests
from bs4 import BeautifulSoup

url = 'http://www.sysports.com.tw/item/oceanya/?lang=zh-hant'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find_all('div', class_='pro-entry')
for i in sb:
    print(i.text, end="")
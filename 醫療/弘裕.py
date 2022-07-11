import requests
from bs4 import BeautifulSoup

url = 'https://www.textile-hy.com.tw/Medical-Garment.htm#con_4945'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find_all('div', class_='lb-overlay')
for i in sb:
    print(i.h3.text)
    print(i.p.text)
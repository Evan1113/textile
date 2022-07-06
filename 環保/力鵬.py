import requests
from bs4 import BeautifulSoup

url = 'https://www.lealeagroup.com.tw/libolon-detail/LIPENGE/'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('div', class_='textEditor')

for i in sb:
   print(i.text , end="")

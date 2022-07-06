import requests
from bs4 import BeautifulSoup

url = 'https://www.tiongliong.com/zh-TW/category/Eco-Friendly-Fabric.html'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('section', class_='section-container')
ab = sb.find('div', class_='row')
a  = ab.find('p', class_='desc').text
print(a)
print()

b  = ab.find('div', class_='display-icon-wrapper clear-fix')
print(b.h4.text)
print()

b1  = ab.find('div', id='item-show')
for i in b1:
   print(i.h5.text)
   print(i.p.text)
   print()


import requests
from bs4 import BeautifulSoup

url = 'https://www.delicacy.com.tw/zh-tw/Product/%E7%92%B0%E4%BF%9D%E7%B4%A0%E6%9D%90/%E7%92%B0%E4%BF%9D%E5%9B%9E%E6%94%B6%E8%81%9A%E9%85%AF'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
title = sp.find('section', id='PDTthree1')
print(title.h3.text)
print()
con = sp.find('div', class_='edit f13 colorGray4c txtCenter')
con1 = con.find_all('p')
for i in con1:
   print(i.text)
print()
print()



url = 'https://www.delicacy.com.tw/zh-tw/Product/%E7%92%B0%E4%BF%9D%E7%B4%A0%E6%9D%90/%E6%9C%89%E6%A9%9F%E6%A3%89'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
title = sp.find('section', id='PDTthree1')
print(title.h3.text)
print()
con = sp.find('div', class_='edit f13 colorGray4c txtCenter')
con1 = con.find_all('p')
for i in con1:
   print(i.text)
print()
print()



url = 'https://www.delicacy.com.tw/zh-tw/Product/%E7%92%B0%E4%BF%9D%E7%B4%A0%E6%9D%90/%E7%92%B0%E4%BF%9D%E5%9E%8B%E6%92%A5%E6%B0%B4'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
title = sp.find('section', id='PDTthree1')
print(title.h3.text)
print()
con = sp.find('div', class_='edit f13 colorGray4c txtCenter')
con1 = con.find_all('p')
for i in con1:
   print(i.text)
print()
print()



url = 'https://www.delicacy.com.tw/zh-tw/Product/%E7%92%B0%E4%BF%9D%E7%B4%A0%E6%9D%90/DL+Cool%E6%B6%BC%E6%84%9F%E7%B4%97%E7%B3%BB%E5%88%97'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
title = sp.find('section', id='PDTthree1')
print(title.h3.text)
print()
con = sp.find('div', class_='edit f13 colorGray4c txtCenter')
con1 = con.find_all('p')
for i in con1:
   print(i.text)


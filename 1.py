import requests
from bs4 import BeautifulSoup
url = 'https://ctee.com.tw/topic/2019tw0050/tex'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
titles = sp.find('div', class_='row vc_row wpb_row vc_row-fluid vc_custom_1571823286988 vc_row-has-fill')
title = titles.find('h3').text
print(title)

a = sp.find('div', class_='row vc_row wpb_row vc_row-fluid vc_custom_1571823286988 vc_row-has-fill')
a1 = a.find_all('h4')
for i in a1:
   print(i.text)
print()
import requests
from bs4 import BeautifulSoup

url = 'http://www.evershineyf.com.tw/EVERSHINE/ProductS.aspx?tid=ELA&sid='
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('div', class_='rightbox')

a  = sb.find('h9_series').text
print(a)
print()

b  = sb.find('div', class_='headbox_Series')
b1 = b.find_all('p')
b2 = b.find_all('h8_series')

for i in range(2):
   print(b2[i].text)
   print(b1[i].text)
   print()





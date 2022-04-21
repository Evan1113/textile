import requests
from bs4 import BeautifulSoup
url = 'https://research.hktdc.com/tc/article/NjU5MjcwMjAw'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
a = sp.find('div', class_="row")
datas = a.find('div', class_="col-12 col-lg-9")
data = datas.find('div', class_="content")
a1 = data.find_all('div', class_="gjs-row")
for i in a1:
   print(i)
print()
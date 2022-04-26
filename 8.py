import requests
from bs4 import BeautifulSoup
url = 'https://www.tipo.org.tw/tc/about_textile_2.aspx'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
a = sp.find('div', class_='box_info')
a1 = a.find('div', class_='box_content')
a2 = a1.find('p')
print(a2[4].text)
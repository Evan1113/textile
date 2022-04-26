import requests
from bs4 import BeautifulSoup
url = 'https://www.materialsnet.com.tw/DocView.aspx?id=47308'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
a = sp.find('div', class_='column col-xs-12')
a1 = a.find_all('div')
print(a1[5].text)
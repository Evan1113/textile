import requests
from bs4 import BeautifulSoup

url = 'https://www.textile-hy.com.tw/Medical-Garment.htm#con_4945'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('div', class_='lb-overlay').text
sc = sp.find_all('h3')
sa = sp.find_all('p')
print(sb)
for i in sc:
    if i.text == '.':
            print()
    else:
        print(i.text)
print()

print(sb)
for i in sa:
    if i.text == '.':
            print()
    else:
        print(i.text)
print()
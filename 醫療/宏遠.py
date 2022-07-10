import requests
from bs4 import BeautifulSoup

url = 'http://www.everest.com.tw/_chinese/00_site/01_edit.aspx?MID=2&SID=10345&TID=10353&ID=10388'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('td', class_='20').text
sc = sp.find_all('font')
print(sb)
for i in sc:
    if i.text == '.':
            print()
    else:
        print(i.text)
print()


url = 'http://www.everest.com.tw/_chinese/00_site/01_edit.aspx?MID=2&SID=10345&TID=10353&ID=10389'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('td', class_='20').text
print(sb)
sc = sp.find_all('p', class_='MsoNormal')
for i in sc:
    if i.text == '.':
        print()
    elif i.text == '':
        print('', end='')
    else:
        print(i.text, end="\n")
print()


url = 'http://www.everest.com.tw/_chinese/00_site/01_edit.aspx?MID=2&SID=10345&TID=10353&ID=10390'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('td', class_='20').text
sc = sp.find_all('font')
print(sb)
for i in sc:
    if i.text == '.':
            print()
    elif i.text == '':
        print('', end='')
    else:
        print(i.text, end="\n")
print()


url = 'http://www.everest.com.tw/_chinese/00_site/01_edit.aspx?MID=2&SID=10345&TID=10353&ID=10391'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('td', class_='20').text
sc = sp.find_all('font')
print(sb)
for i in sc:
    if i.text == '.':
            print()
    elif i.text == '':
        print('', end='')
    else:
        print(i.text, end="\n")
print()


url = 'http://www.everest.com.tw/_chinese/00_site/01_edit.aspx?MID=2&SID=10345&TID=10353&ID=10392'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('td', class_='20').text
print(sb)
sc = sp.find_all('span')
for i in sc:
    if i.text == '.':
        print()
    elif i.text == '':
        print('', end='')
    else:
        print(i.text, end="\n")
print()


url = 'http://www.everest.com.tw/_chinese/00_site/01_edit.aspx?MID=2&SID=10410'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('h1').text
print(sb)
sc = sp.find('font')
for i in sc:
    print(i.text, end="")
print()
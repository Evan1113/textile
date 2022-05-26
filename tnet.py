import requests
from bs4 import BeautifulSoup
for i in range (1,17):
    url = 'https://www.tnet.org.tw/Member/List/99999?page='+str(i)
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    titles = sp.find_all('h4', class_='member-list__title')
    url = sp.find_all('a', class_="member-list__link")
    for n in url:
        print(n.text, end='')
import requests
from bs4 import BeautifulSoup
url = 'https://www.tnet.org.tw/Article/Detail/32773?type=%E7%94%A2%E6%A5%AD%E8%AD%B0%E9%A1%8C_%E7%94%A2%E6%A5%AD%E7%B6%9C%E8%A7%80&species=Slave&backPath=%2FArticle%2FMaster%2F8!%2FArticle%2FSlave%2F8%2F195'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
a = sp.find('main', class_='article__main')
a1 = a.find_all('h3')
a2 = a.find_all('p')
print(a1[2].text)
print(a2[17].text)

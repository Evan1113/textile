import requests
from bs4 import BeautifulSoup
url = 'https://www.tnet.org.tw/Article/Detail/29597?type=%E7%B5%B1%E8%A8%88%E6%95%B8%E6%93%9A%E5%BA%AB_%E7%B5%B1%E8%A8%88%E6%95%B8%E6%93%9A&species=Slave&backPath=%2FArticle%2FMaster%2F9!%2FArticle%2FSlave%2F9%2F175'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
#titles = sp.find('h1', class_='article__title').text
#print(titles)

a = sp.find('main', class_="article__main")
a1 = a.find_all('p')
for i in range(1):
   print(a1[i].text)
print()
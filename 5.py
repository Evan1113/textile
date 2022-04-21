import requests
from bs4 import BeautifulSoup
url = 'https://inboundmarketing.com.tw/%E7%94%A2%E6%A5%AD%E5%B0%88%E6%AC%84/%E5%8F%B0%E7%81%A3%E7%B4%A1%E7%B9%94%E6%A5%AD%E8%A7%80%E9%BB%9E%E5%88%86%E6%9E%90.html'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
data = sp.find('div', class_='elementor-element elementor-element-8f353e5 elementor-widget elementor-widget-theme-post-content')
titles = data.find('div', class_='elementor-widget-container')
a = titles.find_all('h3')
b = titles.find_all('p')
x=1
y=2
for n in range(4):
    print(a[4+x].text)
    print(b[18+y].text)
    y+=2
    x+=1
    print()
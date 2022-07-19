import requests
from bs4 import BeautifulSoup
import re

url = 'https://finance.ettoday.net/news/1553645'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
sb = sp.find('div', class_='story')
con = sb.find("p",string=re.compile("牡蠣殼萃取")).text
print(con)
con = sb.find_all("p",string=re.compile("海洋能量紗")) 
for i in con:
    print(i.text)
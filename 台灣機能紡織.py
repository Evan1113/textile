from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
query = "intitle:台灣機能紡織"
k = []

for j in search(query, stop=1, pause=2.0): 
	print(j)
	k.append(j)

url = k[0]
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0;Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}
r = requests.get(url, headers=headers)

sp = BeautifulSoup(r.text, 'lxml')
con = sp.find_all("p",string=re.compile("機能")) 

for i in con:
   print(i.text)

from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
query = "intitle:儒鴻永續綠色生產"
k = []

for j in search(query, stop=5, pause=2.0): 
	print(j)
	k.append(j)

url = k[0]
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
con = sp.find_all(string=re.compile("永續"))
for i in con:
   print(i)
print()
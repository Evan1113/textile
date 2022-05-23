from googlesearch import search
import requests
from bs4 import BeautifulSoup
import re
query = "intitle:儒鴻永續綠色生產"
# google關鍵字輸入
k = []

for j in search(query, stop=5, pause=2.0): 
	print(j)
	k.append(j)
# google關鍵字查詢結果
url = k[0]
r = requests.get(url)
# 將網站原始碼抓下來
sp = BeautifulSoup(r.text, 'lxml')
con = sp.find_all("p",string=re.compile("永續")) 
# 搜索内容里面包含“永續”的文字
for i in con:
   print(i.text)
print()
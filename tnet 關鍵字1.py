#環保產品 環保材料 環保製程 醫療防護服
import requests
from bs4 import BeautifulSoup
import re

for i in range (1,17):
    url = 'https://www.tnet.org.tw/Member/List/99999?page='+str(i)
    r = requests.get(url)
    sp = BeautifulSoup(r.text, 'lxml')
    sb = sp.find_all('div', class_='col-xs-12',string=re.compile("環保"))
    print(sb)
    for n1 in sb:
        print(n1.h4.text)
        if n1.a == None:
            print()
            print("no URL")
            print()
        else:
            print(n1.a.text)
        print(n1.p.text)
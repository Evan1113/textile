import requests
from bs4 import BeautifulSoup
url = 'https://inboundmarketing.com.tw/%E7%94%A2%E6%A5%AD%E5%B0%88%E6%AC%84/%E5%8F%B0%E7%81%A3%E7%B4%A1%E7%B9%94%E6%A5%AD%E8%A7%80%E9%BB%9E%E5%88%86%E6%9E%90.html'
r = requests.get(url)
sp = BeautifulSoup(r.text, 'lxml')
a = sp.find('spen', id_="qu_shi_yi_zhong_xin_ding_yi_yi_liao_ji_zhi_hui_fu_shi_chao_shi_shang_hua_sheng_huo_hua_fa_zhan")
print(a).text
#a1 = a.find_all('p')
#for i in range(1):
   #print(a1[i].text)
#print()
import requests
url = 'https://inboundmarketing.com.tw/%E7%94%A2%E6%A5%AD%E5%B0%88%E6%AC%84/%E5%8F%B0%E7%81%A3%E7%B4%A1%E7%B9%94%E6%A5%AD%E8%A7%80%E9%BB%9E%E5%88%86%E6%9E%90.html'
r = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if r.status_code == requests.codes.ok:
    print(r.text)
import requests
url = 'https://ctee.com.tw/topic/2019tw0050/tex'
r = requests.get(url)
# 檢查HTTP回應碼是否為200(requests.code.ok)
if r.status_code == requests.codes.ok:
    print(r.text)
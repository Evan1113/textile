import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://knowhowking.com/%E9%86%AB%E5%B8%AB%E6%9C%8D%E6%8E%A8%E8%96%A6/")
soup = BeautifulSoup(response.text, "html.parser")
print(soup.prettify())
import requests
import os
from bs4 import BeautifulSoup

url = "http://www.e-happy.com.tw"
r = requests.get(url)
r.encoding = "utf-8"

dom = BeautifulSoup(r.text, "html5lib")
links = dom.find_all(["a", "img"])
os.system("cls")
print("="*88)

i = 0
for link in links:
    href = link.get("href")
    if href != None:
        i += 1
        print(i, link.get("href"))
print("="*88)

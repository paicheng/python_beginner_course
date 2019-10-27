import requests
import os

os.system("cls")
url = "http://www.e-happy.com.tw"
html = requests.get(url)
html.encoding = "utf-8"
htmllist = html.text.splitlines()
i = 0
for row in htmllist:
    print(i, row)
    i = i+1
    if i > 10:
        break

import requests
import os

os.system("cls")
url = "http://tw.news.yahoo.com"
html = requests.get(url)
html.encoding = "utf-8"

htmllist = html.text.splitlines()
n = 0
for row in htmllist:
    if "台灣" in row:
        n += 1
print("{} times".format(n))

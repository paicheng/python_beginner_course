import re
import os
import requests

os.system("cls")
pat = re.compile("[a-z]+")
m = pat.match("temp12po")
print(m)

regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
url = "https://auth.cht.com.tw/ldaps/"
html = requests.get(url)
html.encoding = "utf-8"
emails = regex.findall(html.text)
for email in emails:
    print(email)

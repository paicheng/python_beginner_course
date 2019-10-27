import requests
import hashlib
import os

url = "https://www.google.com"
html = requests.get(url).text.encode('utf-8-sig')

md5 = hashlib.md5(html).hexdigest()
if os.path.exists("old_md5.txt"):
    with open("old_md5.txt", 'r') as f:
        old_md5 = f.read()

with open("old_md5.txt", 'w') as f:
    f.write(md5)

if md5 != old_md5:
    print("data updated")
else:
    print("dara unchanged")

import requests
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://www.tooopen.com/img/87.aspx"
r = requests.get(url)
r.encoding = "utf-8"

dom = BeautifulSoup(r.text, "html5lib")
images_dir = "images/"
if not os.path.exists(images_dir):
    os.mkdir(images_dir)

all_links = dom.find_all(["a", "img"])
for link in all_links:
    src = link.get("src")
    href = link.get("href")
    attrs = [src, href]
    for attr in attrs:
        if attr != None and (".jpg" in attr or ".png" in attr):
            full_path = attr
            filename = full_path.split("/")[-1]
            print(full_path)

            try:
                image = urlopen(full_path)
                f = open(os.path.join(images_dir, filename), "wb")
                f.write(image.read())
                f.close()
            except:
                print("{} cannot be read.".format(filename))

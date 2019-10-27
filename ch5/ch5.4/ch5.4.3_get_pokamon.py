import os
import requests
from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
from urllib.parse import urlparse

os.system("cls")
dir_name = os.path.dirname(__file__)
url = r"https://tw.portal-pokemon.com/play/pokedex/"
# netloc = urlparse(url).netloc

for id in range(8, 808):
    html = requests.get(url+"{:0>3}".format(id))
    html.encoding = "utf-8"

    soup = bs(html.text, "html5lib")
    name = soup.find("p", {"class": "pokemon-slider__main-name"}).text
    name = "{0:0>3}_{1}".format(id, name)
    src = soup.find("img", {"class": "pokemon-img__front"}).get("src")
    src = "{0[0]}://{0[1]}{1}".format(urlparse(url), src)
    height = soup.find(
        "div", {"class": "pokemon-info__height"}).find_all("span")[1].text
    height = "".join(height.split())
    filename = "{0}_{1}.png".format(name, height)

    mydir = os.path.join(dir_name, "pokemon")
    if os.path.exists(mydir) == False:
        os.mkdir(mydir)
    pathname = os.path.join(mydir, filename)
    try:
        image = urlopen(src)
        f = open(pathname, "bw")
        f.write(image.read())
        f.close()
        print("{} done".format(name))
    except:
        print("{} cannot load".format(name))

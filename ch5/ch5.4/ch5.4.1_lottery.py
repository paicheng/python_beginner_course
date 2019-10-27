import os
import requests
from bs4 import BeautifulSoup

url = "http://www.taiwanlottery.com.tw/"
r = requests.get(url)
r.encoding = "utf-8"

dom = BeautifulSoup(r.text, "html5lib")
data1 = dom.select(".txin")[0]
data2 = data1.find_all("table", {"class": "tableWin"})[0]
data3 = data2.find_all("tr")[4]
data4 = data3.find_all("td")[1]
data5 = data4.find_all("span")
os.system("cls")
for i in range(0, 6):
    print(data5[i].text)

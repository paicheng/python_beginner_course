from urllib.parse import urlparse
import os

os.system("cls")
url = "http://taqm.epa.gov.tw:80/pm25/tw/PM25A.aspx?area=1"
pm25 = urlparse(url)
print(pm25)

print("scheme= {}".format(pm25.scheme))
print("netloc= {}".format(pm25.netloc))
print("path= {}".format(pm25.path))
print("path= {}".format(pm25[-2]))
# print(urlparse("http://www.google.com"))

import ast
import hashlib
import os
import sqlite3

import requests
from bs4 import BeautifulSoup

dir_name = os.path.dirname(__file__)
new_path = os.path.join(dir_name, "pm25.sqlite3")
conn = sqlite3.connect(new_path)
conn.execute('''
    CREATE TABLE IF NOT EXISTS t_pm25 (
        "no" integer primary key,
        "sitename" text,
        "pm25" integer
        )
    ''')

url = r"http://opendata.epa.gov.tw/webapi/Data/ATM00679/?$orderby=MonitorDate%20desc&$skip=0&$top=1000&format=json"
html = requests.get(url)
html.encoding = "utf-8"
html = html.text.encode("utf-8")
# html = html.encode("utf-8")
md5 = hashlib.md5(html).hexdigest()
old_md5 = ""

md5_path = os.path.join(dir_name, "old_md5.txt")
if os.path.exists(md5_path):
    with open(md5_path, "r") as f:
        old_md5 = f.read()
with open(md5_path, "w") as f:
    f.write(md5)

if old_md5 != md5:
    print("it is new data...")
    soup = BeautifulSoup(html, "html5lib")
    jsondata = ast.literal_eval(soup.text)
    conn.execute("DELETE FROM t_pm25")
    conn.commit()

    n = 1
    for site in jsondata:
        siteid = site["SiteId"]
        sitename = site["SiteName"]
        pm25 = 0 if site["PM25SubIndex"] == "" else int(site["PM25SubIndex"])
        print("id: {}\t site: {}\t pm2.5: {}".format(siteid, sitename, pm25))
        sql = "INSERT INTO t_pm25 (no, sitename, pm25)VALUES ({}, '{}', {});".format(
            n, sitename, pm25)
        conn.execute(sql)
        n += 1
        conn.commit()
else:
    print("data is old...")
    cursor = conn.execute("SELECT * FROM t_pm25;")
    rows = cursor.fetchall()
    for row in rows:
        print("site: {}\t pm2.5: {}".format(row[1], row[2]))

conn.close()

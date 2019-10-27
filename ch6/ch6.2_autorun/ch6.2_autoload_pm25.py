import os
import sqlite3
import requests
import ast
import hashlib
from bs4 import BeautifulSoup as bs
from datetime import datetime

mydir = os.path.dirname(__file__)

url = r"http://opendata.epa.gov.tw/webapi/Data/ATM00679/?$orderby=MonitorDate%20desc&$skip=0&$top=1000&format=json"
html = requests.get(url).text.encode("utf-8")

md5 = hashlib.md5(html).hexdigest()
# print(md5)
old_md5 = ""
md5_path = os.path.join(mydir, "old_md5.txt")
if os.path.exists(md5_path):
    with open(md5_path, "r") as f:
        old_md5 = f.read()

with open(md5_path, "w") as f:
    f.write(md5)
    # pass

if md5 != old_md5:
    soup = bs(html, "html5lib")
    json = ast.literal_eval(soup.text)
    # print(type(json[0]))
    db_path = os.path.join(mydir, "db.sqlite3")
    conn = sqlite3.connect(db_path)

    sql = """
        create table if not exists t_pm25 (
            "no" integer primary key,
            "date" text,
            "sitename" text,
            "pm25" integer,
            "insert_on" text
        )"""
    conn.execute(sql)
    conn.commit()

    for site in json:
        sitename = site["SiteName"]
        date = site["MonitorDate"]
        pm25 = 0 if site["PM25SubIndex"] == "" else int(site["PM25SubIndex"])
        sql = """
            INSERT INTO t_pm25 ('sitename', 'date', 'pm25', 'insert_on') 
            VALUES('{}', '{}', {}, '{}')
            """.format(sitename, date, pm25, str(datetime.now()))
        # print(sql)
        conn.execute(sql)
    conn.commit()
    conn.close()

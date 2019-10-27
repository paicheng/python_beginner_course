from selenium import webdriver
from time import sleep
import os

os.system("cls")
urls = ["http://www.google.com", "http://www.e-happy.com.tw",
        "http://opendata.epa.gov.tw", "https://tw.yahoo.com/"]

browser = webdriver.Chrome()
browser.maximize_window()

# browser.get("https://www.microsoft.com")
n = 1
for url in urls:
    browser.get(url)
    browser.get_screenshot_as_file(r"C:\Users\paich\Desktop\{}.png".format(n))
    n = n+1
    sleep(3)
input()
browser.quit()

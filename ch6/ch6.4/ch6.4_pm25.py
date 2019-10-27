from selenium import webdriver
from time import sleep
import os

os.system("cls")
url = "https://opendata.epa.gov.tw"
chrome = webdriver.Chrome()
chrome.get(url)

sleep(3)
try:
    mylink = chrome.find_element_by_partial_link_text("空氣品質")
    mylinks.click()
    sleep(3)
    input()
except:
    pass
finally:
    chrome.quit()

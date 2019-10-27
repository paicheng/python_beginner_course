from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os

os.system("cls")
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
browser.get("https://www.microsoft.com")
browser.get_screenshot_as_file(r"C:\Users\paich\Desktop\test-selenium.png")
browser.quit()

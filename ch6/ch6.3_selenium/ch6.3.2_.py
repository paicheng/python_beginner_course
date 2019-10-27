from selenium import webdriver
import os

os.system("cls")

browser = webdriver.Chrome()
browser.get(
    r"C:/Users/paich/Documents/python_beginner_course/ch6/ch6.3/myhtml.html")

login_form = browser.find_element_by_id("loginForm")
# print(login_form.text)

username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

login_form = browser.find_element_by_xpath("//form[@id='loginForm']")
username = browser.find_element_by_xpath("//input[@name='username']")
# print(login_form.text)
# print(username.text)

continue_link = browser.find_element_by_link_text("Continue")
# print(continue_link.get_attribute("href"))

continue_link_part = browser.find_element_by_partial_link_text("Cont")
print(continue_link_part.get_attribute("href"))

browser.find_element_by_tag_name("a")
browser.find_elements_by_class_name("content")
browser.find_elements_by_css_selector(".content")

browser.quit()

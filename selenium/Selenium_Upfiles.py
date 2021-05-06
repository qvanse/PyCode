from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
wd=webdriver.Chrome()
wd.implicitly_wait(5)
wd.get(' https://tinypng.com/')
ele=wd.find_element_by_css_selector('input[type=file]')
ele.send_keys(r'f:\1.png')

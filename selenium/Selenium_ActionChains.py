from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
wd=webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('https://www.baidu.com/')
ac=ActionChains(wd)
ac.move_to_element(wd.find_element_by_css_selector('[name="tj_briicon"]')).perform()

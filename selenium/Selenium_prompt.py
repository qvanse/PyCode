from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
wd=webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/test4.html')
wd.find_element_by_id('b3').click()
print(wd.switch_to.alert.text)
wd.switch_to.alert.send_keys('Web自动化-Selenium')
wd.switch_to.alert.accept()
wd.find_element_by_id('b3').click()
wd.switch_to.alert.dismiss()


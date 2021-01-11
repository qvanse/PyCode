from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
wd=webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/test4.html')
wd.find_element_by_id('b1').click() #点击按钮
print(wd.switch_to.alert.text) #打印对话框文本
wd.switch_to.alert.accept() #点击对话框确定按钮

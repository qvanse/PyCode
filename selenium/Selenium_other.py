from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
wd=webdriver.Chrome()
wd.implicitly_wait(5)
wd.get('http://cdn1.python3.vip/files/selenium/test4.html')
print(wd.get_window_size())
wd.set_window_size(800,600)
print(wd.title)
print(wd.current_url)
wd.get_screenshot_as_file('1.jpg')

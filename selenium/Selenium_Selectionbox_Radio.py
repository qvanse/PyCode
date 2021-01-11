from selenium import webdriver

#用于Radio单选框的选择
url='http://cdn1.python3.vip/files/selenium/test2.html'
wd=webdriver.Chrome()
wd.get(url)
element=wd.find_element_by_css_selector('#s_radio input[checked="checked"]')
print("当前选择的是："+element.get_attribute("value"))

wd.find_element_by_css_selector('#s_radio input[value="小雷老师"]').click()

from selenium import webdriver

#用于Radio单选框的选择
url='http://cdn1.python3.vip/files/selenium/test2.html'
wd=webdriver.Chrome()
wd.get(url)
#单条复选框去除。
#wd.find_elements_by_css_selector("#s_checkbox input[checked='checked']").click()

#多条复选框，通过循环去除。
elements=wd.find_elements_by_css_selector("#s_checkbox input[checked='checked']")
for element in elements:
    print(element.get_attribute('outerHTML'))
    element.click()


wd.find_element_by_css_selector("#s_checkbox input[value='小雷老师']").click()




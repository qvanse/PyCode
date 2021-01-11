from selenium import webdriver
from selenium.webdriver.support.ui import Select
#用于Radio单选框的选择
url='http://cdn1.python3.vip/files/selenium/test2.html'
wd=webdriver.Chrome()
wd.get(url)
#单选框的操作
select=Select(wd.find_element_by_id('ss_single'))
select.select_by_visible_text("小雷老师")
#多选框的操作
m_select=Select(wd.find_element_by_id('ss_multi'))
m_select.deselect_all()
m_select.select_by_visible_text('小雷老师')
m_select.select_by_visible_text('小凯老师')

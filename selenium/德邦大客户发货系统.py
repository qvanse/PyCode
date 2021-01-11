from selenium import webdriver
import time
wd=webdriver.Chrome()
wd.implicitly_wait(3)
wd.get('https://vip.deppon.com/vas-cas-web/login')
wd.find_element_by_css_selector(".account_num_icon.vas_bg+input").send_keys("15226545252")
wd.find_element_by_css_selector(".password_icon.vas_bg+input").send_keys("zhao134*")
time.sleep(2)
link=wd.find_element_by_css_selector(".submit.btn.btn-dpyellow").click()

#.templateBNav.transitionBGColor:nth-child(4)>.transitionMaxHeight>.templateBSecondNav.transitionBGColor>div
wd.switch_to.window(wd.window_handles[0])
#https://www.cnblogs.com/lirongyang/p/12651634.html



















































#操作frame/iframe框架
# wd.get('http://f.python3.vip/webauto/sample2.html')
# wd.switch_to.frame(wd.find_element_by_tag_name('iframe'))
# elements=wd.find_elements_by_css_selector('.plant')
# for element in elements:
#     print('-----------')
#     print(element.get_attribute('outerHTML'))
# # print(elements.get_attribute('outerHTML'))
# #elements.send_keys('你好！')
# wd.switch_to.default_content()
# wd.find_element_by_css_selector('#outerbutton').click()
# time.sleep(10)
# wd.quit()

#切换新网页操作
# elements=wd.find_element_by_tag_name('a').click()
# print(wd.title)
# print(wd.current_url)
# mainWindow=wd.current_window_handle
#
# for handle in wd.window_handles:
#     print(handle)
#     wd.switch_to.window(handle)
#     if 'Bing' in wd.title:
#         break
# print(wd.title)
# wd.find_element_by_id("sb_form_q").send_keys("白月黑羽")
# wd.switch_to.window(mainWindow)
# wd.find_element_by_id('outerbutton').click()
# # time.sleep(5)
# wd.quit()
###############窗口的点击。
# wd.find_element_by_id("b1").click()
# print(wd.switch_to.alert.text)
# wd.switch_to.alert.accept()
###############
# wd.find_element_by_id("b3").click()
# print(wd.switch_to.alert.text)
# print('点击确定！')
# wd.switch_to.alert.send_keys("光复香港，时代革命！")
# wd.switch_to.alert.accept()
# time.sleep(5)
# wd.find_element_by_id("b3").click()
# print(wd.switch_to.alert.text)
# print("点击取消！")
# wd.switch_to.alert.dismiss()



























































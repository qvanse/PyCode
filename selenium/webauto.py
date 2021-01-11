from selenium import webdriver
import time
#######################################################【爬取评议页面】################################################
url='https://cl.jxnel.com/htm_data/0805/20/131469.html' 
pageurl=[]
pageurl.append(url)
urlTemp='https://cl.jxnel.com/read.php?tid='
tid=url.split('/')[6].split('.')[0]
wd=webdriver.Chrome()
wd.get(url)   #自己下载下来的网页
wd.implicitly_wait(3)
#elements=wd.find_elements_by_css_selector('#cate_6 .tr3.f_one>th>h2')    #爬取主页草榴休閑區
#elements=wd.find_elements_by_css_selector('#cate_1 .icon.tac+th>h2')    #爬取主页BT電影下載
pages=wd.find_element_by_css_selector('.w70>input').get_attribute('value').split('/')[1]
pages=int(pages)+1
'''
https://cl.nx63.xyz/htm_data/2010/16/4131883.html   #帖子第一页
https://cl.nx63.xyz/read.php?tid=4131883&page=2 #帖子第二页
'''
for page in range(2,pages):
    pageurl.append(urlTemp+tid+'&page='+str(page))
print(pageurl)
#########################################################【爬取用户名】###################################################
username=[]
for urlT in pageurl:
    wd.get(urlT)
    elements=wd.find_elements_by_css_selector('.tr1.do_not_catch>th>b')    #爬取用户名
    for element in elements:
        username.append('element.text')
        
        #username.append(element.text)
print(username)
       





from selenium import webdriver
import time
url='https://detail.1688.com/offer/600455574455.html?spm=a2615.2177701.autotrace-offerGeneral.9.3e9674c5vSiSmW'
wd=webdriver.Chrome()
wd.implicitly_wait(5)
wd.get(url)
elements=wd.find_elements_by_css_selector('[max-width="790"]')
for i in elements:
    print(i)
    



# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 22:44:40 2019

@author: guojige
"""

#coding:utf-8

from selenium import webdriver

import time

 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time 

#option = webdriver.ChromeOptions()
#option.set_headless()
#options=option

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless') # chrome_options=chrome_options
browser = webdriver.Chrome()
try:
    #browser.get('https://bj.lianjia.com/zufang/BJ2288876426621370368.html')
    browser.get('https://bj.lianjia.com/zufang/BJ2276614472955068416.html?nav=0')
    #time.sleep(3)
    #input1 = browser.find_element_by_xpath('//*[@id="around"]/ul/li').text
    #input2 = browser.find_element_by_xpath("//div[@class='content__map']")
    #browser.f
    input3 = browser.find_element_by_id("map") #
    #input4 = browser.find_element_by_xpath("//div[@class='content__map--overlay']") #content__map--overlay
    browser.maximize_window()  
    browser.execute_script("arguments[0].scrollIntoView();",input3)#移动到元素element对象的“顶端”与当前窗口的“顶部”对齐
    #time.sleep(3)
    #input4 = browser.find_element_by_xpath("//div[@class='content__map--overlay']")
    #print(input2)
    #print(input3)
    #print(input4) #
    #input5 = browser.find_element_by_xpath('//*[@id="mapDetail"]/div[3]/div[2]/ul[1]/li[2]')
    time.sleep(4)
    #wait = WebDriverWait(browser, 1)
    browser.find_element_by_xpath("//li[@data-href='around']").click()
    #input2.click()
    #input.send_keys('Python')
    #input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 1)
    #print(input5)
    #print(input1)
    #input5.click()
    
    browser.find_element_by_xpath("//li[@data-key='公交站']").click()
    time.sleep(3)
    
    input6 = browser.find_element_by_xpath('//*[@id="mapDetail"]/div[3]/div[2]/ul[2]/li[1]/p[1]/span').text
    print(input6)
    input7 = browser.find_element_by_xpath('//li[@data-index="0"]/p[1]').text
    print(input7)
    #wait.until(EC.presence_of_element_located((By.XPATH('/html/body/div[6]/div/div[2]/ul[1]/li[1]/a'))))
    #print(browser.current_url)
    #print(browser.get_cookies())
    #print(browser.page_source)
finally:
    browser.close()
    #pass




#driver.implicitly_wait(8)

 


 


#driver.execute_script("scroll(0,2400)")#大概的拖动

#driver.execute_script("arguments[0].scrollIntoView(false);",ele)#移动到元素element对象的“底端”与当前窗口的“底部”对齐

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")#移动到页面最底部
    
    
#  https://www.cnblogs.com/Rita-LJ/p/7884995.html
#  https://www.cnblogs.com/eastmount/p/4810690.html  
#  https://blog.csdn.net/weixin_36279318/article/details/79475388
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 18:00:45 2019

@author: guojige
"""

"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


brguge=webdriver.Chrome()#声明驱动对象
try:
    brguge.get('https://www.baidu.com')#发送get请求
    input=brguge.find_element_by_id('kw')#找到目标

    input.send_keys('python')#输入python关键字
    input.send_keys(Keys.ENTER)#敲入回车
    wait=WebDriverWait(brguge,10)#等待元素加载出来
    wait.until(EC.presence_of_element_located(By.ID,'content_left'))#加载
    print(brguge.current_url)#输出搜索的路径
    #print(brguge.get_cookie())#输出cookie
    #print(brguge.page_source)#输出结果源代码
finally:
    brguge.close()#关闭谷歌浏览器

"""



from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
 
browser = webdriver.Chrome()
try:
    browser.get('https://www.baidu.com')
    input = browser.find_element_by_id('kw')
    input.send_keys('Python')
    input.send_keys(Keys.ENTER)
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
    print(browser.current_url)
    print(browser.get_cookies())
    print(browser.page_source)
finally:
    browser.close()
    


"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time 

#chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless') # chrome_options=chrome_options
browser = webdriver.Chrome()
try:
    browser.get('https://bj.lianjia.com/zufang/BJ2288439389254328320.html')
    #time.sleep(3)
    input1 = browser.find_element_by_xpath('//*[@id="around"]/ul/li').text
    input2 = browser.find_element_by_xpath("//div[@class='content__map']")
    input3 = browser.find_element_by_id("map") #
    input4 = browser.find_element_by_xpath("//div[@class='content__map--overlay']") #content__map--overlay
    
    #print(input2)
    print(input3)
    print(input4)
    #input2.click()
    #input.send_keys('Python')
    #input.send_keys(Keys.ENTER)
    #wait = WebDriverWait(browser, 5)
    print(input1)
    #wait.until(EC.presence_of_element_located((By.XPATH('/html/body/div[6]/div/div[2]/ul[1]/li[1]/a'))))
    #print(browser.current_url)
    #print(browser.get_cookies())
    #print(browser.page_source)
finally:
    browser.close()
"""

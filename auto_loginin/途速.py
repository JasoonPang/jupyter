# -*- coding: utf-8 -*-
"""
Created on Sun Apr 22 02:39:54 2018

@author: 724719274@qq.com
"""

import time
from selenium import webdriver
#import webbrowser
#  
#driver = webbrowser.open("https://tsocks.tpcontrol.net/auth/login") 
driver = webdriver.Chrome()
driver.open('https://tsocks.tpcontrol.net/auth/login')  #需要打开的网址
time.sleep(5)

def sign_in(email): 
    driver.find_element_by_id("email").clear()
    driver.find_element_by_id("email").send_keys(email)
    #driver.find_element_by_id("passwd").send_keys(keys.ENTER)
    driver.find_element_by_id("passwd").clear()
    driver.find_element_by_id("passwd").send_keys("pzhs8517100")
    driver.find_element_by_id("login").click()
    print('登录成功')
    
def check():
    driver.find_element_by_xpath("//*[@class='btn btn-block btn-outline btn-primary']").click()
    time.sleep(3)
    driver.find_element_by_xpath("//button[2]").click()
    print('签到成功')

def sign_out():
    driver.find_element_by_xpath("//*[@class='fa fa-sign-out']").click() #登出
    print('登出')

for email in ['1@qq.com','5@qq.com', '2@qq.com','3@qq.com',\
              '6@qq.com', '4@qq.com','724719274@qq.com']:#
    sign_in(email)    
    time.sleep(10)
    if '立即签到' in driver.page_source:
        check()
    elif "不能签到" in driver.page_source:
        print('已签')        
    time.sleep(1)     
    sign_out()           
        
driver.close()
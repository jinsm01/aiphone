#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/16 18:12 
# @Author :labixiaoxin
# @File : test_cap.py
# from time import sleep
from time import sleep

from appium import webdriver
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-7555'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
desired_caps['noReset'] = True  # 记住之前动作，缓存数据
desired_caps['dontStopAppOnReset'] = True

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys('alibaba')
sleep(5)

driver.quit()





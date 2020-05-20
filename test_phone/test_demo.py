#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/16 14:42 
# @Author :labixiaoxin
# @File : test_demo.py

from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'emulator-7555'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = 'com.android.settings.Settings'
desired_caps['appPackage'] = 'com.xueqiu.android'
desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
desired_caps['noReset'] = True

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(10)

el1 = driver.find_element_by_id("com.xueqiu.android:id/home_search")
el1.click()
el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
el2.send_keys("alibaba")
el3 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.RelativeLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]")
el3.click()

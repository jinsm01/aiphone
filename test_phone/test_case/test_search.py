#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 14:01 
# @Author :labixiaoxin
# @File : test_search.py
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By


class TestSearch:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # 首次启动时，不停止app，调试或运行时提升速度
        desired_caps['dontStopAppOnReset'] = True
        # 是否在测试前后重置环境，默认重置
        desired_caps['noReset'] = True
        # 输入中文字符
        desired_caps['unicodeKeyBoard'] = True
        # 测试完重置输入法
        desired_caps['resetKeyBoard'] = True
        #跳过权限设置、安装等操作，调试或运行提升速度
        desired_caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()  #回到首页
        self.driver.quit()

    def test_search(self):
        print('search case')
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('阿里巴巴')
        # self.driver.find_element(By.XPATH, '//*[@resource-id="com.xueqiu.android:id/stockName" and @text="阿里巴巴"]').click()
        curr_price = self.driver.find_element(By.ID, 'com.xueqiu.android:id/current_price').text
        print(curr_price)
        assert float(curr_price) > 200

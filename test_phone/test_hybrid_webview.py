#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 14:42
# @Author  : shaonianlang
# @File    : test_hybrid_webview.py

from time import sleep

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.mobile import Mobile
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps = {}
        des_caps['platformName'] = 'Android'
        des_caps['platformVersion'] = '6.0'
        des_caps['deviceName'] = 'emulator-7555'
        des_caps['noReset'] = True
        # des_caps['appPackage'] = 'io.appium.android.apis'
        # des_caps['appActivity'] = '.view.WebView1'
        des_caps['appPackage'] = 'com.xueqiu.android'
        des_caps['appActivity'] = '.common.MainActivity'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)

        self.driver.implicitly_wait(10)

    def teardown(self):
        # pass
        self.driver.quit()



    def test_xueqiu_kaihu(self):
        print(self.driver.contexts)
        self.driver.find_element(By.XPATH, '//*[@text="交易"]').click()
        print(self.driver.contexts)


    #
    # def test_browser(self):
    #     print(self.driver.contexts)
    #     self.driver.switch_to.context(self.driver.contexts[-1])
    #     self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys('这是一个混合应用测试')
    #     self.driver.find_element(MobileBy.ID, 'i am a link').click()
    #     print(self.driver.page_source)
    #


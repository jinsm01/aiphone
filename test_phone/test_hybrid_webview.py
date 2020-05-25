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
        des_caps['chromedriverChromeMappingFile'] = r'E:\xuexi\aiphone\test_phone\mapping.json'
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)

        self.driver.implicitly_wait(10)

    def teardown(self):
        pass
        # self.driver.quit()

    def test_create_account(self):
        # 点击交易
        self.driver.find_element(By.XPATH, '//*[@text="交易"]').click()
        print(self.driver.contexts)
        # 切换上下文，原生-webview
        self.driver.switch_to.context((self.driver.contexts)[-1])
        # 显示等待
        locator = (MobileBy.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        # 点击webview中的开户
        old_handles = self.driver.window_handles
        self.driver.find_element(MobileBy.XPATH, '//*[@id="Layout_app_3V4"]/div/div/ul/li[1]/div[2]').click()
        new_handles = self.driver.window_handles
        # 获取句柄
        for curr_handles in new_handles:
            if curr_handles in old_handles:
                pass
            else:
                handles = curr_handles
                self.driver.switch_to.window(handles)
        input_locator = (MobileBy.ID, 'phone-number')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(input_locator))
        self.driver.find_element(MobileBy.ID, 'phone-number').send_keys('134444444444')
        self.driver.find_element(MobileBy.ID, 'code').send_keys('111111')
        self.driver.find_element(MobileBy.XPATH, '/html/body/div/div/div[2]/div/div[2]').click()


    # def test_browser(self):
    #     print(self.driver.contexts)
    #     self.driver.switch_to.context(self.driver.contexts[-1])
    #     self.driver.find_element(MobileBy.ID, 'i_am_a_textbox').send_keys('这是一个混合应用测试')
    #     self.driver.find_element(MobileBy.ID, 'i am a link').click()
    #     print(self.driver.page_source)
    #


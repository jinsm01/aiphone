#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 12:26
# @Author  : shaonianlang
# @File    : test_webview.py
from time import sleep

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestBrowser:
    def setup(self):
        des_caps = {}
        des_caps['platformName'] = 'Android'
        des_caps['platformVersion'] = '6.0'
        des_caps['deviceName'] = 'emulator-7555'
        des_caps['browserName'] = 'browser'
        des_caps['chromedriverChromeMappingFile'] = r'E:\xuexi\aiphone\test_phone\mapping.json'
        des_caps['noReset'] = True

        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)

        self.driver.implicitly_wait(10)

    def teardown(self):
        self.driver.quit()

    def test_browser(self):
        self.driver.get('http://m.baidu.com')
        sleep(5)
        self.driver.find_element(By.ID, 'index-kw').click()
        self.driver.find_element(By.ID, 'index-kw').send_keys('Appium')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'index-bn')))
        self.driver.find_element(By.ID, 'index-bn').click()

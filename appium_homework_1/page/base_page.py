#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 0:39
# @Author  : shaonianlang
# @File    : base_page.py
from appium import webdriver


class BasePage:
    def __init__(self):
        des_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'devicesName': 'emulator-7555',
                    'appPackage': 'com.xueqiu.android', 'appActivity': '.common.MainActivity', 'noReset': True,
                    'unicodeKeyBoard': True, 'resetKeyBoard': True, 'dontStopAppOnReset': True,
                    'skipDeviceInitialization': True}
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des_caps)
        self.driver.implicitly_wait(10)

    def find(self, by, locator):
        return self.driver.find_element(by, locator)

    def back(self):
        return self.driver.back()

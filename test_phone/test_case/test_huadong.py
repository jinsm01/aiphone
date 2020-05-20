#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 16:24 
# @Author :labixiaoxin
# @File : test_huadong.py

import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By


class TestSearch:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-7555'
        desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
        desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_touchaction(self):
        action = TouchAction(self.driver)
        action.press(x=123, y=167).wait(200).move_to(x=360, y=167).wait(200).move_to(x=604, y=167).wait(200)\
               .move_to(x=604, y=414).wait(200).move_to(x=604, y=654).release().perform()
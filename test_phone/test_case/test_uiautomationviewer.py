#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 17:29 
# @Author :labixiaoxin
# @File : test_uiautomationviewer.py
from time import sleep

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
        desired_caps['appPackage'] = 'com.sina.weibo'
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        desired_caps['appActivity'] = '.page.SuperPageActivity'
        # 首次启动时，不停止app，调试或运行时提升速度
        desired_caps['dontStopAppOnReset'] = True
        # 是否在测试前后重置环境，默认重置
        desired_caps['noReset'] = True
        # 输入中文字符
        desired_caps['unicodeKeyBoard'] = True
        # 测试完重置输入法
        desired_caps['resetKeyBoard'] = True
        # 跳过权限设置、安装等操作，调试或运行提升速度
        desired_caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        # self.driver.find_element_by_android_uiautomator('new UiSelector().description("发现")').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("本地")').click()

        self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().description('
            '"两只猫一起泡澡").instance(0))').click()
        # self.driver.find_element_by_android_uiautomator('new UiSelector().text("东先生")').click()


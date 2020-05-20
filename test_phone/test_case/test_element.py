#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/18 15:36 
# @Author :labixiaoxin
# @File : test_element.py
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
        # 跳过权限设置、安装等操作，调试或运行提升速度
        desired_caps['skipDeviceInitialization'] = True
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.back()  # 回到首页
        self.driver.quit()

    @pytest.mark.skip
    def test_search(self):
        print(self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').is_enabled())

        print(self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').get_attribute('name'))

        print(self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').location)

        print(self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').size)

        self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
        a = self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('alibaba')
        if a.is_displayed() == True:
            print('搜索成功')
        else:
            print('搜索失败')

    def test_touchaction(self):
        action = TouchAction(self.driver)
        # action.press(x=378.5, y=1109).wait(60000).move_to(x=378.5, y=255.8).perform()
        window_rect = self.driver.get_window_rect()
        width = window_rect['width']
        height = window_rect['height']
        x1 = int(width / 2)
        y_start = int(height * 4 / 5)
        y_end = int(height * 1 / 5)
        action.press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).perform()

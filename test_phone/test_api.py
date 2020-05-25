#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 17:38
# @Author  : shaonianlang
# @File    : test_api.py
from time import sleep

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions


class TestMobile:
    def setup(self):

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'emulator-7555'
        # desired_caps['appPackage'] = 'com.xueqiu.android'
        # desired_caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
        # desired_caps['noReset'] = True  # 记住之前动作，缓存数据
        # desired_caps['dontStopAppOnReset'] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def test_mobile(self):
        # self.driver.make_gsm_call('13900000000', GsmCallActions.CALL)
        # self.driver.send_sms('13600000000', '短信内容')


        sleep(7)
        self.driver.start_recording_screen()
        self.driver.set_network_connection(1)
        sleep(7)
        self.driver.stop_recording_screen()
        self.driver.set_network_connection(2)

        sleep(7)
        self.driver.set_network_connection(4)
        self.driver.get_screenshot_as_file("./'截图1.png")
        sleep(7)
        self.driver.set_network_connection(2)




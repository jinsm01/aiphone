#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 14:43 
# @Author :labixiaoxin
# @File : test_hamrest.py
from hamcrest import *

#
# class TestHamresst:
#     def test_hamrest(self):
#         # assert_that(10, equal_to(10))
#         # assert_that(10, equal_to(9), '10不等于9')
#         # assert_that( 8 , close_to( 10, 2 ))


class TestWait:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['devicesName'] = '127.0.0.1:7555'
        desired_caps['appPackage'] = 'com.xueqiu.android'
        desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
        desired_caps['automationName'] = 'Uiautomator2'
        desired_caps['noReset'] = True
        desired_caps['dontStopAppOnReset'] = True
        desired_caps['skipDeviceInitialization'] = True
        desired_caps['unicodeKeyBoard'] = True
        desired_caps['resetKeyBoard'] = True
        self.driver = webdriver.Remote('127.0.0.1:4723/wd/hub', desired_caps)

        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

      #  // *[ @ text = "00772"] /../../..// *[ @ resource - id = "com.xueqiu.android:id/current_price"]
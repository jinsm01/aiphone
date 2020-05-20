#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/19 10:10 
# @Author :labixiaoxin
# @File : test_wait.py

from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


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

    # def test_wait(self):
    #     loactor = (MobileBy.XPATH, '//*[@text="我的"]')
    #     WebDriverWait(self.driver, 10).until(
    #         expected_conditions.element_to_be_clickable(loactor))
    #     # self.driver.find_element(By.ID, 'com.xueqiu.android:id/tv_search').click()
    #     # self.driver.find_element(By.ID, 'com.xueqiu.android:id/search_input_text').send_keys('yuewen')
    #     # self.driver.find_element(By.XPATH, '//*[@text="阅文集团"]').click()
    #
    # def test_alert(self):
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="我的"]').click()
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/iv_setting').click()
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="设置登录密码"]').click()
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/new_password').send_keys('123456789qazxcv')
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/confirm_new_password').send_keys('123456789qazxcv')
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/login').click()
    #     a = self.driver.find_element(MobileBy.XPATH, '//*[@text="密码需包含字母和数字，长度8至16位"]').text
    #     assert a == '密码需包含字母和数字，长度8至16位'

    # def test_login(self):
    #     loactor = (MobileBy.XPATH, '//*[@text="我的"]')
    #     WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(loactor))
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="我的"]').click()
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="登录雪球"]').click()
    #     self.driver.find_element(MobileBy.ID, 'com.xueqiu.android:id/login_password').send_keys('123456789qazxcv')
    #     self.driver.find_element(MobileBy.XPATH, '//*[@text="登录"]').click()
    #     toast_message = '登录成功'
    #     message = '//*[@text=\'{}\']'.format(toast_message)
    #     toast_element = WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(message))
    #     print(toast_element.text)

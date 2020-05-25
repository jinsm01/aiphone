#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 17:02
# @Author  : shaonianlang
# @File    : test_weixin.py
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


class TestWeixin:
    def setup(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0'
        desired_caps['deviceName'] = 'emulator-7555'
        desired_caps['appPackage'] = 'com.tencent.wework'
        desired_caps['appActivity'] = '.launch.WwMainActivity'
        desired_caps['noReset'] = True
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        self.driver.implicitly_wait(10)


    def teardown(self):
        self.driver.quit()




    def test_weixin(self):
        # 点击通讯录
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        # 点击添加成员
        self.driver.find_element_by_android_uiautomator('new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))').click()
        # 点击手动输入添加
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        # 输入姓名   //*[@text="姓名　"]/..//*[@text="必填"]
        self.driver.find_element(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@text="必填"]').send_keys('封装')
        # 选择性别  //*[@text="男"]   //*[@text="女"]
        self.driver.find_element(MobileBy.XPATH, '//*[@text="男"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="女"]').click()
        # 输入手机号   com.tencent.wework:id/eqx
        self.driver.find_element(MobileBy.ID, 'com.tencent.wework:id/eqx').send_keys('18799979899')
        # 点击保存
        self.driver.find_element(MobileBy.XPATH, '//*[@text="保存"]').click()
        # Toast //*[@class="android.widget.Toast"]
        self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]')



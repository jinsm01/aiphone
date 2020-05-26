#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 18:55
# @Author  : shaonianlang
# @File    : app.py
from appium import webdriver

from appium_homework_2.page.base_page import BasePage
from appium_homework_2.page.main_page import MainPage


# app 启动
class APP(BasePage):
    def start_app(self):
        if self.driver is None:
            desired_caps = {'platformName': 'Android', 'platformVersion': '6.0', 'deviceName': 'emulator-7555',
                            'appPackage': 'com.tencent.wework', 'appActivity': '.launch.WwMainActivity',
                            'noReset': True}

            self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
        else:
            self.driver.launch_app()
        self.driver.implicitly_wait(10)
        return self

    def restart_app(self):
        return self

    def stop_app(self):
        return self

    # 进入主页面
    def main_windows(self):
        return MainPage(self.driver)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 13:39
# @Author  : shaonianlang
# @File    : app.py
import yaml
from appium import webdriver

from UI测试框架.page.base_page import BasePage
from UI测试框架.page.main import Main


class App(BasePage):
    _appPackage = "com.xueqiu.android"
    _appActivity = ".view.WelcomeActivityAlias"

    def start(self):
        # 第二次调用stat时判断是否存在driver
        if self._driver is None:
            caps = dict()
            caps['platformName'] = 'Android'
            caps['platformVersion'] = '6.0'
            caps['deviceName'] = 'emulator-7555'
            caps['appPackage'] = self._appPackage
            caps['appActivity'] = self._appActivity
            caps['noReset'] = True
            caps['udid'] = yaml.safe_load(open("../page/configuration.yaml"))['caps']['udid']
            self._driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
            self._driver.implicitly_wait(3)
        else:
            self._driver.start_activity(self._appPackage, self._appActivity)
        return self

    def restart_app(self):
        pass

    def stop_app(self):
        pass

    def main(self) -> Main:
        return Main(self._driver)
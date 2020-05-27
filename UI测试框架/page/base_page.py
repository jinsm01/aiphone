#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 13:37
# @Author  : shaonianlang
# @File    : base_page.py
import yaml
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    _driver: WebDriver
    _back_list = [(By.ID, "iv_close")]

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # 元素查找，通用方法封装
    def find(self, locator, value: str = None):
        try:
            if isinstance(locator, tuple):
                element = self._driver.find_element(*locator)
            else:
                element = self._driver.find_element(locator, value)
            return element
        except:
            for black in self._back_list:
                element = self._driver.find_elements(*black)
                if len(element) > 0:
                    element[0].click()
                    break
            return self.find(locator, value)


    # 步骤解析
    def steps(self, path):
        with open(path) as f:
            steps = yaml.safe_load(f)
        element = None
        for step in steps:
            if "by" in step.keys():
                element = self.find(step["by"], step["locator"])
            if "action" in step.keys():
                action = step["action"]
                if action == "click":
                    element.click()

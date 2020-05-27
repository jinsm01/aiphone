#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 13:37
# @Author  : shaonianlang
# @File    : base_page.py
from appium.webdriver.webdriver import WebDriver


class BasePage:
    _driver: WebDriver

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def find(self, locator, value: str = None):
        if isinstance(locator, tuple):
            return self._driver.find_element(*locator)
        else:
            return self._driver.find_element(locator, value)

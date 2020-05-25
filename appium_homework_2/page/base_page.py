#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 21:03
# @Author  : shaonianlang
# @File    : base_page.py
from appium.webdriver.webdriver import WebDriver


class BasePage:
    def __init__(self, driver: WebDriver = None):
        self.driver = driver
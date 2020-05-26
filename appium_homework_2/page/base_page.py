#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 21:03
# @Author  : shaonianlang
# @File    : base_page.py
import logging

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By


class BasePage:
    logging.basicConfig(level=logging.INFO)
    # 已知未知弹窗
    back_list = [(MobileBy.XPATH, '//*[@text="确定"]'),
                 (MobileBy.XPATH, '//*[@text="取消"]'),
                 (MobileBy.XPATH, '//*[@text="确认"]')]

    max_num = 3
    error_num = 0

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        try:
            if isinstance(locator, tuple):
                element = self.driver.find_element(*locator)

            else:
                element = self.driver.find_element(locator, value)
            self.error_num = 0
            self.driver.implicitly_wait(10)
            return element
        except Exception as e:
            self.driver.implicitly_wait(1)
            if self.error_num > self.max_num:
                raise e
            self.error_num += 1
            for ele in self.back_list:
                logging.info(ele)
                ele_list = self.driver.find_elements(*ele)
                if len(ele_list) > 0:
                    ele_list[0].click()
                    return self.find(locator, value)
            raise e



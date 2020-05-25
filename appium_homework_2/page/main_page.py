#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 18:56
# @Author  : shaonianlang
# @File    : main_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_homework_2.page.address_book_page import AdressBook


# app主页
from appium_homework_2.page.base_page import BasePage


class MainPage(BasePage):
    def goto_message(self):
        pass

    # 跳转到通讯录
    def goto_adressbook(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="通讯录"]').click()
        return AdressBook(self.driver)

    def goto_workbench(self):
        pass

    def goto_mine(self):
        pass

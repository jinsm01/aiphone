#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 19:15
# @Author  : shaonianlang
# @File    : add_menus_page.py
from appium.webdriver.common.mobileby import MobileBy
from appium_homework_2.page.base_page import BasePage



class AddMenus(BasePage):
    def input_name(self, name):
        self.find(MobileBy.XPATH, '//*[@text="姓名　"]/..//*[@text="必填"]').send_keys(name)
        return self

    def select_gender(self):
        self.find(MobileBy.XPATH, '//*[@text="男"]').click()
        self.find(MobileBy.XPATH, '//*[@text="女"]').click()
        return self

    def input_numbers(self, number):
        self.find(MobileBy.ID, 'com.tencent.wework:id/eqx').send_keys(number)
        return self

    def save_button(self):
        from appium_homework_2.page.add_members_page import AddMembers
        self.find(MobileBy.XPATH, '//*[@text="保存"]').click()
        return AddMembers(self.driver)

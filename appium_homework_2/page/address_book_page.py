#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 19:21
# @Author  : shaonianlang
# @File    : address_book_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_homework_2.page.add_members_page import AddMembers
from appium_homework_2.page.base_page import BasePage
from appium_homework_2.page.personal_info_page import PersonalInfo


class AdressBook(BasePage):
    # 点击添加成员
    def add_members_button(self):
        element = self.driver.find_element_by_android_uiautomator(
            'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().text("添加成员").instance(0))')
        element.click()
        return AddMembers(self.driver)

    def select_member(self, selename):
        self.driver.find_element(MobileBy.XPATH, f'//*[@text="{selename}"]').click()
        return PersonalInfo(self.driver)

    def get_all_members(self):
        return len(self.driver.find_elements(MobileBy.ID, 'com.tencent.wework:id/d8_'))



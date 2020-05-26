#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 10:47
# @Author  : shaonianlang
# @File    : edit_member_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_homework_2.page.base_page import BasePage


class EditMember(BasePage):
    def delete_button(self):
        from appium_homework_2.page.address_book_page import AdressBook
        self.driver.find_element(MobileBy.XPATH, '//*[@text="删除成员"]').click()
        self.driver.find_element(MobileBy.XPATH, '//*[@text="确定"]').click()
        return AdressBook(self.driver)





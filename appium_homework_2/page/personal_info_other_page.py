#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 10:43
# @Author  : shaonianlang
# @File    : personal_info_other_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_homework_2.page.base_page import BasePage
from appium_homework_2.page.edit_member_page import EditMember


class PersonalInfoOther(BasePage):
    def edit_member(self):
        self.driver.find_element(MobileBy.XPATH, '//*[@text="编辑成员"]').click()
        return EditMember(self.driver)
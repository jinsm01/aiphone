#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/26 10:40
# @Author  : shaonianlang
# @File    : personal_info_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_homework_2.page.base_page import BasePage
from appium_homework_2.page.personal_info_other_page import PersonalInfoOther


class PersonalInfo(BasePage):
    def other_button(self):
        self.find(MobileBy.ID, 'com.tencent.wework:id/gvd').click()
        return PersonalInfoOther(self.driver)
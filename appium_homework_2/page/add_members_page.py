#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 19:11
# @Author  : shaonianlang
# @File    : add_members_page.py
from appium.webdriver.common.mobileby import MobileBy

from appium_homework_2.page.base_page import BasePage


class AddMembers(BasePage):
    def weixin_invite(self):
        pass

    def address_list_invite(self):
        pass

    # 点击手动添加方式
    def add(self):
        from appium_homework_2.page.add_menus_page import AddMenus
        self.driver.find_element(MobileBy.XPATH, '//*[@text="手动输入添加"]').click()
        return AddMenus(self.driver)

    def get_toast(self):
        # return self.driver.find_element(MobileBy.XPATH, '//*[@text="添加成功"]').text
        return self.find(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text

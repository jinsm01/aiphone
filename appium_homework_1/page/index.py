#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/21 22:36
# @Author  : shaonianlang
# @File    : index.py


from appium.webdriver.common.mobileby import MobileBy
from appium_homework_1.page.base_page import BasePage


class Index(BasePage):
    content = None

    def test_search(self, search_content):
        self.find(MobileBy.ID, 'com.xueqiu.android:id/tv_search').click()
        self.find(MobileBy.ID, 'com.xueqiu.android:id/search_input_text').send_keys(search_content)
        self.find(MobileBy.ID, 'com.xueqiu.android:id/name').click()
        self.content = self.find(MobileBy.ID, 'com.xueqiu.android:id/stockName').text
        self.back()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 13:49
# @Author  : shaonianlang
# @File    : main.py
from selenium.webdriver.common.by import By

from UI测试框架.page.base_page import BasePage


class Main(BasePage):
    def goto_search(self):
        # 步骤驱动调用点击
        # self.find(By.ID, 'tv_search').click()
        self.steps("../page/main.yaml")

    def goto_window(self):

        self.find(By.ID, 'post_status').click()
        self.find(By.ID, 'tv_search').click()
        #
        # self.steps("../page/main.yaml")

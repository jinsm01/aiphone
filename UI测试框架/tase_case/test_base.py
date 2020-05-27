#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 16:18
# @Author  : shaonianlang
# @File    : test_base.py
from UI测试框架.page.app import App


class TestBase:
    app = None

    def setup(self):
        self.app = App()

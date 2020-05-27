#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 14:01
# @Author  : shaonianlang
# @File    : test_main.py
from UI测试框架.page.app import App


class TestMain:

    def test_main(self):
        app = App()
        app.start().main().goto_search()

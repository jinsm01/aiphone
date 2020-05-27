#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 14:01
# @Author  : shaonianlang
# @File    : test_main.py
import pytest
import yaml

from UI测试框架.page.app import App

class TestMain:

    @pytest.mark.parametrize('value1, value2', yaml.safe_load(open("../tase_case/test_main.yaml")))
    def test_values(self, value1, value2):
        print(value2)
        print(value1)

    def test_main(self):
        app = App()
        app.start().main().goto_search()

    def test_window(self):
        app = App()
        app.start().main().goto_window()
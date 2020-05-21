#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/22 0:47
# @Author  : shaonianlang
# @File    : test_search.py
import pytest
from appium_homework_1.page.index import Index


class TestSearch:
    def setup(self):
        self.index = Index()

    @pytest.mark.parametrize('search_content', ['阿里巴巴', '阅文集团'])
    def test_search(self, search_content):
        self.index.test_search(search_content)
        assert search_content == self.index.content




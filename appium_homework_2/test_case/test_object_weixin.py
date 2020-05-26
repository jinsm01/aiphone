#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/25 19:26
# @Author  : shaonianlang
# @File    : test_object_weixin.py
from appium_homework_2.page.app import APP


class TestWeiXin:
    def setup(self):
        self.app = APP()
        self.main = self.app.start_app().main_windows()

    def teardown(self):
        pass

    def test_add_member(self):
        result = self.main.goto_adressbook().add_members_button().add()\
            .input_name().input_numbers().select_gender().save_button().get_toast()
        print(result)
        assert result == '添加成功'

    def test_delete_member(self):
        before_num = self.main.goto_adressbook().get_all_members()
        self.main.goto_adressbook().select_member().other_button().edit_member().delete_button()
        after_num = self.main.goto_adressbook().get_all_members()
        assert after_num == before_num - 1

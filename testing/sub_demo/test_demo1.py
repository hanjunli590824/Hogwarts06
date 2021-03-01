#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 17:58
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_demo1.py
# @software: PyCharm

import pytest


@pytest.fixture()
def connectDB():
    print("test_demo1 中的connectDB")

def test_a():
    print("sub_demo test_a")

class TestA:
    def test_b(self,connectDB):
        print("sub_demo test_b")
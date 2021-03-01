#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 22:23
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_params.py
# @software: PyCharm
import pytest

@pytest.fixture(params=[1, 2, 3])
def login1(request):
    data = request.param
    print(request.param)
    print("获取测试数据")
    return data

def test_case1(login1):
    print(login1)
    print("测试用例1")
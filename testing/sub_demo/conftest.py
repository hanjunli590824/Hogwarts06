#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 17:59
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : conftest.py
# @software: PyCharm
import pytest


@pytest.fixture()
def connectDB():
    print("sub_demo 下面的connectDB")
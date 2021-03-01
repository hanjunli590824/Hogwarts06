#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 17:35
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_assume.py
# @software: PyCharm
import pytest


def test_a():
    # assert 1 == 2
    # assert False == True
    # assert 100 == 200
    pytest.assume(1 == 1)
    pytest.assume(False == True)
    pytest.assume(100 == 200)
    pytest.assume(3 == 1)
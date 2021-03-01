#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 17:46
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_ordering.py
# @software: PyCharm
from time import sleep

import pytest


@pytest.mark.run(order=10)
def test_1():
    sleep(1)
    assert True

# @pytest.mark.third
def test_2():
    sleep(1)
    assert True

@pytest.mark.run(order=9)
def test_3():
    sleep(1)
    assert True
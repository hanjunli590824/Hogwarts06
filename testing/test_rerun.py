#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 17:16
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_rerun.py
# @software: PyCharm

# 插件
# -pytest-rerunfailures
# pytest test_rerun.py --reruns 3 --reruns-delay 1

# -xdist---用例之间是独立的，没有依赖关系，因为执行的时候没有顺序
# pytest test_ordering.py -n 3


from time import sleep

import pytest


def test_rerun1():
    sleep(0.5)
    assert 1 == 2

def test_rerun2():
    sleep(0.5)
    assert 2 == 2

@pytest.mark.flaky(reruns=5, reruns_delay=2)
def test_rerun3():
    sleep(0.5)
    assert 3 == 2
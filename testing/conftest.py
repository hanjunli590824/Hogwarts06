#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 17:34
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : conftest.py
# @software: PyCharm

# conftest.py用法
# -conftest.py文件名不能变
# -conftest.py与运行的用例要在同一个package下
# -不需要import导入conftest.py，pytest用例会自动查找
# -所有同目录测试文件运行前都会执行conftest.py文件
# -全局的配置和前期工作都可以写在这里

# pytest配置
# -写在pytest.ini文件中
# -放在项目工程的根目录
# -不能用任何的中文符号


import pytest

from python_code.calc import Calculator


@pytest.fixture(scope="session")
def connectDB():
    print("链接数据库操作")
    yield
    print("断开数据库操作")


@pytest.fixture(scope='class')
def get_calc():
    print('获取计算器实例')
    calc = Calculator()
    return calc
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 17:17
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_scope.py
# @software: PyCharm

# fixture
# 调用方式
# -测试用例中传入fixture方法名
# -‘@pytest.mark.usefixtures("方法名")’
# -自动调用：‘@pytest.fixture(autouse=True)’
#
# 作用域
# -控制方法：‘@pytest.fixture(scope=‘’)’
# -scope的取值
#  -function
#  -class
#  -module
#  -session
#
# fixture方法返回值的获取
# -在测试用例中使用fixture方法名就可以获取到yield后面的返回值


class TestDemo:

    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")

class TestDemo1:

    def test_a(self, connectDB):
        print("测试用例a")

    def test_b(self, connectDB):
        print("测试用例b")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/27 16:11
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : t_yield.py
# @software: PyCharm

# yield 生成器
def provider():
    # 循环读取数据
    for i in range(10):
        print("开始操作")
        yield i
        print("结束操作")

# 普通函数调用
p = provider()
# print(p)
print(next(p))
print(next(p))
print(next(p))
print(next(p))
print(next(p))
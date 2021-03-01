#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/2/28 14:50
# @Author  : Lance
# @Email   : 670955423@qq.com
# @File    : test_calc_new.py
# @software: PyCharm

# allure
# -生成 allure 测试结果：pytest --alluredir=./result
# -展示报告：allure serve ./result
# -生成最终版本的报告：allure generate ./result
# -清除上一次的记录：allure generate --clean result -o result/html

import allure
import pytest
import yaml


with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)['add']
    add_datas = datas['datas']
    print(add_datas)
    myid = datas['myid']
    print(myid)

@pytest.fixture(params=add_datas, ids=myid)
def get_datas(request):
    print('开始计算')
    data = request.param
    print(f"测试数据为:{data}")
    yield data
    print('结束计算')

@allure.feature("测试计算器")
class TestCalc:

    """
    优化点：
    -把setup和teardown换成了fixture方法get_calc
    -把get_calc方法放到了conftest中
    -把参数化换成了fixture参数化方式
    -测试用例中的数据需要通过get_datas获取
    get_datas返回了一个列表[1,2,3],分别代表了a,b,expect
    """
    @allure.story("测试加法")
    @pytest.mark.add
    def test_add(self, get_calc, get_datas):
        # 调用add方法
        with allure.step("计算两个数的相加和"):
            result = get_calc.add(get_datas[0], get_datas[1])
        # 判断result是浮点数，做出保留两位小数的处理
        if isinstance(result, float):
            result = round(result, 2)
        # 断言
        assert result == get_datas[2]
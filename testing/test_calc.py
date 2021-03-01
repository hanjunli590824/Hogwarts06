
# pytest运行
# pytest规则
# -测试文件、测试函数、测试方法名程需要以test_开头
# -测试类名称需要以Test开头
# -测试类中不能包含__init__方法
#
# pycharm中运行
# 1.运行整个测试文件，在文件上点击鼠标右键，选择run
# 2.点击绿色小三角，运行对应的测试类或者测试方法
#
# 命令行运行
# -运行当前目录下所有测试文件：pytest
# -运行指定的测试文件：pytest 文件名（注：要注意路径）
# -运行指定文件中的指定的类或者方法：pytest 文件名::测试类名::测试方法名
# -查看执行过程中的详细信息和打印信息：pytest -vs
# -只收集测试用例不运行：pytest --collect-only
# -生成执行结果文件：testing>pytest --junitxml=./result.xml

# pytest 框架结构
# -模块级别（setup_module/teardown_module）模块始末，全局的（有限最高）
# -函数级别（setup_function/teardown_function）只对函数用例生效（不在类中）
# -类级别（setup_class/teardown_class）只在类前后执行一次（在类中）
# -方法级别（setup_method/teardown_method）开始于方法始末（在类中）
# -类里面（setup/teardown）运行在调用方法的前后

# 参数化
# -单个参数化：参数名称写在字符串中，参数值用列表传递
# -多个参数：参数名称写在字符串中，参数值用列表嵌套列表或者元组的方式传递
# -测试用例起别名：ids=
# -笛卡尔积：用两个装饰器分别传入参数
# -从yaml中读取参数：数据读取成为参数化中需要的参数格式

import pytest
import yaml

from python_code.calc import Calculator

with open("./datas/calc.yaml") as f:
    datas = yaml.safe_load(f)
    adddatas = datas['add']
    add_data = adddatas['add_datas']
    print(add_data)
    addmyid = adddatas['add_myid']
    print(addmyid)

    divdatas = datas['div']
    div_data = divdatas['div_datas']
    print(div_data)
    divmyid = divdatas['div_myid']
    print(divmyid)

# def test_a():
#     print("测试用例a")

class TestCalc:

    def setup_class(self):
        # 实例化计算器类
        self.calc = Calculator()

    def setup(self):
        print("计算开始")

    def teardown(self):
        print("计算结束")

    @pytest.mark.parametrize(
        "a,b,expect",
        add_data,ids=addmyid
    )
    @pytest.mark.add
    def test_add(self,a,b,expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用add方法
        if isinstance(a, str):
            print("a必须为数字类型")
            assert False
        elif isinstance(b, str):
            print("b必须为数字类型")
            assert False
        elif a > 9999 or a < -9999:
            print("a不能超过4位数字")
            assert False
        elif b > 9999 or b < -9999:
            print("b不能超过4位数字")
            assert False
        else:
            result = self.calc.add(a, b)
            # 判断result是浮点数，做出保留两位小数的处理
            if isinstance(result, float):
                result = round(result, 2)
            # 断言
            assert result == expect

    @pytest.mark.parametrize(
        "a, b, expect",
        div_data,ids=divmyid
    )
    @pytest.mark.div
    def test_div(self,a,b,expect):
        # 实例化计算器类
        # calc = Calculator()
        # 调用div方法
        if isinstance(a, str):
            print("a必须为数字类型")
            assert False
        elif isinstance(b, str):
            print("b必须为数字类型")
            assert False
        elif b == 0:
            print("b不能为0")
            assert False
        elif a > 9999 or a < -9999:
            print("a不能超过4位数字")
            assert False
        elif b > 9999 or b < -9999:
            print("b不能超过4位数字")
            assert False
        else:
            result = self.calc.div(a, b)
            # 判断result是浮点数，做出保留两位小数的处理
            if isinstance(result,float):
                result = round(result,2)
            # 断言
            assert result == expect

    # def test_add2(self):
    #     result = self.calc.add(0.1,0.2)
    #     assert round(result,2) == 0.3

    # @pytest.mark.add
    # def test_add1(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(0.1, 0.1)
    #     # 断言
    #     assert result == 0.2
    #
    # @pytest.mark.add
    # def test_add2(self):
    #     # 实例化计算器类
    #     # calc = Calculator()
    #     # 调用add方法
    #     result = self.calc.add(-1, -1)
    #     # 断言
    #     assert result == -2
    #
    # @pytest.mark.div
    # def test_div(self):
    #     print("test_div")
    #
    # @pytest.mark.sub
    # def test_sub(self):
    #     print("test_sub")
    #
    # @pytest.mark.mul
    # def test_mul(self):
    #     print("test_mul")
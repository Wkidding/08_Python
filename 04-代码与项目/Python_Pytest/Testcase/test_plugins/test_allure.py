# -*- coding: UTF-8 -*-
"""===============================================
@Author ：kidding
@Date   ：2026/8/1 18:36
@File   ：test_allure.py
@IDE    ：PyCharm
=================================================="""
"""
测试pytest常用插件 - allure报告allure-pytest
"""

import pytest
import allure
from os.path import basename
from allure_commons.types import Severity
from allure_commons.types import LabelType
from allure_commons.types import ParameterMode


# def test_allure_a():
#     print("--test_allure_a")
#     assert 1 == 2
#
# def test_allure_b():
#     print("--test_allure_b")
#     assert 1 == 1
#
# class Test01:
#     def test_allure_d(self):
#         print("--test_allure_d")
#         assert False
#
#     def test_allure_c(self):
#         print("--test_allure_c")
#         assert "cs" in "adcsbill"




class Test02:
    def test_allure_success (self):
        assert 1 == 1

    def test_allure_fail (self):
        assert 1 == 2

def test_allure_skip ( ):
    pytest.skip("---skip")

@pytest.mark.xfail(1 == 1, reason="---xfail")
def test_allure_xfail ( ):
    # pytest.xfail("---xfail")
    1 == 2

def test_allure_broken ( ):
    raise Exception("---exception")

def test_allure_error ( ):
    assert a == "asfssfcs"


class Test03:
    # 静态方式：使用装饰器
    @allure.title("测试用户登录功能")
    def test_login(self):
        pass

    # 参数化测试中动态替换标题
    @pytest.mark.parametrize("username", ["admin", "guest"])
    @allure.title("登录测试 - 用户 {username}")
    def test_login_with_params(self,username):
        pass

    # 动态方式：在函数体内设置
    def test_dynamic_title(self):
        allure.dynamic.title("动态设置的测试标题")
        assert True

class Test04:
    @allure.description("""
    # 登录功能测试

    ## 测试步骤
    1. 打开登录页面
    2. 输入用户名和密码
    3. 点击登录按钮

    ## 预期结果
    登录成功，跳转到首页
    """)
    def test_login_description (self):
        pass

    # 动态方式
    def test_dynamic_description (self):
        allure.dynamic.description("测试失败时截图保存")
        assert True

class Test05:
    @allure.tag("冒烟测试", "回归测试", "登录模块")
    def test_login (self):
        pass


class Test06:
    @allure.severity(Severity.CRITICAL)
    def test_critical_function(self):
        pass

    @allure.severity(Severity.BLOCKER)
    def test_blocker_function(self):
        pass

    @allure.severity(Severity.MINOR)
    def test_minor_function(self):
        pass


class Test07:
    @allure.link("https://docs.example.com/api", name="API文档")
    @allure.issue("BUG-12345", name="关联缺陷")
    @allure.testcase("TC-67890", name="测试用例")
    def test_with_links(self):
        pass

class Test08:
    @allure.label(LabelType.LANGUAGE, "python")
    @allure.label(LabelType.FRAMEWORK, "pytest")
    @allure.label("owner", "测试团队")
    def test_with_custom_label (self):
        pass

class Test09:
    @allure.epic("电商平台")
    @allure.feature("订单管理")
    @allure.story("创建订单")
    def test_create_order (self):
        pass

    @allure.epic("电商平台")
    @allure.feature("订单管理")
    @allure.story("取消订单")
    def test_cancel_order (self):
        pass


class Test10:
    @allure.parent_suite("Web接口测试")
    @allure.suite("用户模块")
    @allure.sub_suite("登录相关")
    def test_login_api (self):
        pass


class TestShopping:
    @allure.step("步骤1：打开商品详情页")
    def open_product_page (self, product_id):
        print(f"打开商品 {product_id}")

    @allure.step("步骤2：点击加入购物车")
    def add_to_cart (self):
        print("加入购物车")

    @allure.step("步骤3：验证购物车数量")
    def verify_cart_count (self, expected):
        print(f"验证购物车数量为 {expected}")

    def test_shopping_flow (self):
        self.open_product_page("P001")
        self.add_to_cart()
        self.verify_cart_count(1)


class Test11:
    def test_login_flow (self):
        with allure.step("打开登录页面"):
            print("打开 https://example.com/login")

        with allure.step("输入用户名和密码"):
            print("输入 admin / 123456")

        with allure.step("点击登录按钮"):
            print("点击登录")

        with allure.step("验证登录成功"):
            assert True


class Test12:
    @pytest.mark.parametrize("username,password", [
        ("admin", "正确密码"),
        ("admin", "错误密码"),
    ])
    @allure.title("登录测试 - {username} / {password}")
    def test_login_parametrized (self, username, password):
        pass


class Test13:
    def test_with_dynamic_param (self):
        allure.dynamic.parameter("环境", "预发布环境")
        allure.dynamic.parameter("浏览器", "Chrome")
        assert True


class Test14:
    def test_with_sensitive_param (self):
        allure.dynamic.parameter(
            "password",
            "********",
            mode=ParameterMode.MASKED
        )
        assert True



class Test15:
    @pytest.fixture()
    @allure.title("准备测试数据 - 创建测试用户")
    def test_user (self):
        user = { "name": "test_user", "email": "test@example.com" }
        yield user
        # 清理操作

    def test_with_fixture (self, test_user):
        assert test_user["name"] == "test_user"





class Test16:
    def test_with_attachments(self):
        # 附加文本
        allure.attach("这是一条日志信息", name="执行日志", attachment_type=allure.attachment_type.TEXT)

        # 附加 JSON
        import json
        data = { "status": "success", "code": 0 }
        allure.attach(
            json.dumps(data, indent=2),
            name="响应数据",
            attachment_type=allure.attachment_type.JSON
        )

        # 附加 HTML
        allure.attach(
            "<div style='color:green'>测试通过</div>",
            name="HTML片段",
            attachment_type=allure.attachment_type.HTML
        )

        assert True




class Test17:
    def test_with_file_attachment(self):
        # 附加截图文件
        allure.attach.file(
            "screenshot.png",
            name="页面截图",
            attachment_type=allure.attachment_type.PNG
        )

        # 附加日志文件
        allure.attach.file(
            "test.log",
            name="测试日志",
            attachment_type=allure.attachment_type.TEXT
        )
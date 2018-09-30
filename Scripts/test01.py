import allure
import pytest

class Test000():
    @allure.step("执行学院新增操作")
    def test01(self):
        print("test01被执行了")

    @allure.step("执行学院更新操作")

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test03(self):
        allure.attach("断言开始","断言是否更新")
        print("test02被执行了")
        allure.attach("断言结束","断言更新成功")

import logging
import unittest
import app
from api.employee import EmployeeApi
from api.login_api import LoginApi

from utils import assert_common, create_phone


class TestIHRMEmp(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()
        cls.employee_api = EmployeeApi()

    # 登陆成功
    def test_01_login_success(self):
        jsonData = {"mobile": "13800000002", "password": "123456"}
        headers = {"Content-type": "application/json"}
        response = self.login_api.login(jsonData, headers)
        # 打印响应数据
        logging.info("登录成功的结果为：{}".format(response.json()))
        token = "Bearer " + response.json().get("data")
        app.HEADERS = {"Content-type": "application/json", "Authorization": token}
        logging.info("请求头为：{}".format(app.HEADERS))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 添加员工
    def test_02_add_emp(self):
        response = self.employee_api.add_emp("测试username", create_phone(), app.HEADERS)
        logging.info("添加员工后的结果为：{}".format(response.json()))
        app.EMP_ID = response.json().get("data").get("id")
        logging.info("添加员工后的id为：{}".format(app.EMP_ID))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 查询员工
    def test_03_query_emp(self):
        response = self.employee_api.query_emp(app.EMP_ID, app.HEADERS)
        logging.info("查询员工后的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 修改员工
    def test_04_update_emp(self):
        jsonData = {"username": "修改后username"}
        response = self.employee_api.modify_emp(app.EMP_ID, jsonData=jsonData, headers=app.HEADERS)
        logging.info("修改员工后的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

    # 删除员工
    def test_05_delete_emp(self):
        response = self.employee_api.delete_emp(app.EMP_ID, app.HEADERS)
        logging.info("删除员工后的结果为：{}".format(response.json()))
        assert_common(self, 200, True, 10000, "操作成功", response)

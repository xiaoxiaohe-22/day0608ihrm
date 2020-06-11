import logging
import unittest
from parameterized import parameterized
from api.login_api import LoginApi
from app import BASE_PATH
from utils import assert_common, get_login_data


class TestIHRMLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.login_api = LoginApi()

    # 参数化
    @parameterized.expand(get_login_data(BASE_PATH + "/data/login_data.json"))
    def test_login(self, case_name, request_body, success, code, message, http_code):
        headers = {"Content-type": "application/json"}
        response = self.login_api.login(request_body, headers)
        # 打印响应数据
        logging.info("{}的结果为：{}".format(case_name, response.json()))
        # 断言
        assert_common(self, http_code, success, code, message, response)

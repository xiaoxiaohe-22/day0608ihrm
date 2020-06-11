import os

# 设置全局变量工程根目录
import requests

BASE_PATH = os.path.abspath(os.path.dirname(__file__))

# 设置整个项目得域名
ihrm_url = "http://ihrm-test.itheima.net"

HEADERS = None
EMP_ID = None


# 获取令牌的方法
class GetToken:
    __token = None

    @classmethod
    def get_token(cls):
        if cls.__token is None:
            response = requests.post(url=ihrm_url + "/api/sys/login",
                                     json={"mobile": "13800000002", "password": "123456"})
            # print(response.json())  # 'data': '513c1b77-499b-49d7-b262-b05e0988ae05'
            # 保存令牌
            cls.__token = "Bearer " + response.json().get("data")
        print("令牌是:", cls.__token)
        return cls.__token

import requests
from requests import Response

from app import ihrm_url


class EmployeeApi(object):
    def __init__(self):
        # 定义员工模块的URL
        self.emp_url = ihrm_url + "/api/sys/user"

    # 新增员工接口
    def add_emp(self, username, mobile, headers):
        """
        :rtype Response
        """
        # 根据外部传入的username和mobile拼接成要发送的请求体数据
        jsonData = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-05-05",
            "formOfEmployment": 1,
            "departmentName": "测试部",
            "departmentId": "1063678149528784896",
            "correctionTime": "2020-05-30T16:00:00.000Z"
        }
        return requests.post(url=self.emp_url, json=jsonData, headers=headers)

    # 查询员工接口
    def query_emp(self, emp_id, headers):
        return requests.get(url=self.emp_url + "/" + emp_id, headers=headers)

    # 修改员工接口
    def modify_emp(self, emp_id, jsonData, headers):
        # 拼接修改员工的URL
        modify_url = self.emp_url + "/" + emp_id
        # 发送修改员工的接口请求，并 return返回结果
        return requests.put(url=modify_url, json=jsonData, headers=headers)

    # 删除员工接口
    def delete_emp(self, emp_id, headers):
        # 拼接删除员工的URL
        delete_url = self.emp_url + "/" + emp_id
        # 发送删除员工的接口请求，return返回数据
        return requests.delete(url=delete_url, headers=headers)

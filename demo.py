import requests

from app import ihrm_url, GetToken

# 实现添加员工接口
response_add = requests.post(url=ihrm_url + "/api/sys/user",
                             json={"username": "尼古拉的地方划我们", "mobile": "15528565269", "timeOfEntry": "2020-05-05",
                                   "formOfEmployment": 1, "departmentName": "测试部",
                                   "departmentId": "1063678149528784896",
                                   "correctionTime": "2020-05-30T16:00:00.000Z"},
                             headers={"Content-Type": "application/json", "Authorization": GetToken.get_token()})

print("添加成功后结果为:", response_add.json())

emp_id = response_add.json().get("data").get("id")
print('员工id为:', emp_id)

# 查询员工接口
response_query = requests.get(url=ihrm_url + "/api/sys/user/" + emp_id,
                              headers={"Content-Type": "application/json", "Authorization": GetToken.get_token()})
print("查询员工的结果为:", response_query.json())

# 修改员工接口
response_update = requests.put(url=ihrm_url + "/api/sys/user/" + emp_id,
                               headers={"Content-Type": "application/json", "Authorization": GetToken.get_token()},
                               json={"username": "修改后尼古拉的规划我们"})
print("修改员工的结果为:", response_update.json())

# 删除员工接口
response_delete = requests.delete(url=ihrm_url + "/api/sys/user/" + emp_id,
                                  headers={"Content-Type": "application/json", "Authorization": GetToken.get_token()})
print("删除员工的结果为:", response_delete.json())
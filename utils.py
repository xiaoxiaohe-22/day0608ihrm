import json
import logging
import random
from logging import handlers
from app import BASE_PATH


# 配置日志的格式
def basic_log_config():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    # 设置处理器
    sh = logging.StreamHandler()
    file_name = BASE_PATH + "/log/ihrm.log"
    tf = logging.handlers.TimedRotatingFileHandler(filename=file_name, when="M", interval=1, backupCount=3,
                                                   encoding="utf-8")
    # 创建格式化器
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s")
    sh.setFormatter(formatter)
    tf.setFormatter(formatter)
    logger.addHandler(sh)
    logger.addHandler(tf)


# 封装通用得断言模块代码
def assert_common(self, status_code, success, code, message, response):
    self.assertEqual(status_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


# 随机生成手机号
def create_phone():
    # 第二位数字
    second = [3, 4, 5, 7, 8][random.randint(0, 4)]
    # 第三位数字
    third = {
        3: random.randint(0, 9),
        4: [5, 7, 9][random.randint(0, 2)],
        5: [i for i in range(10) if i != 4][random.randint(0, 8)],
        7: [i for i in range(10) if i not in [4, 9]][random.randint(0, 7)],
        8: random.randint(0, 9),
    }[second]
    # 最后八位数字
    suffix = random.randint(9999999, 100000000)
    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


# 读取login_data数据
def get_login_data(filename):
    with open(file=filename, encoding="utf-8") as f:
        data_list = []
        json_load = json.load(f)
        for ele in json_load:
            data_list.append(list(ele.values()))
        return data_list


# 编写读取员工模块的数据函数
def read_emp_data(filepath, interface_name):
    # 打开数据文件
    with open(filepath, mode='r', encoding='utf-8') as f:
        # 把数据文件加载成json格式
        jsonData = json.load(f)
        # 读取加载的json数据当中对应接口的数据
        emp_data = jsonData.get(interface_name)  # type:dict
        # 把数据处理成列表元组对象，然后添加到空列表当中
        result_list = list()
        result_list.append(tuple(emp_data.values()))
    return result_list


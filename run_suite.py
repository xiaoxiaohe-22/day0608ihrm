import time
import unittest

from BeautifulReport import BeautifulReport

from app import BASE_PATH

test_suite = unittest.TestLoader().discover(start_dir=BASE_PATH + "/script/", pattern="test_ihrm_employee.py")
file_name = "report-{}.html".format(time.strftime("%Y%m%d %H%M%S"))
BeautifulReport(test_suite).report(filename=file_name, log_path=BASE_PATH + "/log",description="员工的增删改查")

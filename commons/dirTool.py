import os
from os.path import dirname, abspath

# 框架项目顶层目录的绝对路径
root_path = dirname(dirname(abspath(__file__)))

#测试数据路径
data_path = os.path.join(root_path,'apiData')

#测试用例路径
test_case_path = os.path.join(root_path,'test_case')

#测试报告临时文件路径
test_temporary_report = os.path.join(root_path,'output/report/temporaryAllureFile')

#allure测试报告路径
report_path = os.path.join(root_path,'output/report/allureResult')

#congig配置文件地址
config_path = os.path.join(root_path,'configs')
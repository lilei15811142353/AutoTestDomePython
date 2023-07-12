# -- coding: utf-8 --**
import os
import sys
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)

import pytest
from commons.larkRobotMsg import *
from commons.operationProcess import *
from commons.dateTimeTool import *
from commons.dirTool import *



def generate_report(case_name):
    path = os.getcwd()  # 项目APi路径
    log.logger.info(path)
    nowData = DateTimeTool().get_now_date()
    nowTime = DateTimeTool().get_now_secondTime().replace(":","-")

    #
    # tempath = os.path.join(path, r"output/report/temporaryAllureFile/{}/{}".format(nowData, nowTime))  # 报告临时存放文件
    tempath = test_temporary_report + r"/{}/{}".format(nowData, nowTime)  # 报告临时存放文件
    log.logger.info('临时文件存放路径：' + tempath)

    # reportpath = os.path.join(path, r"output/report/allureResult/{}/{}".format(nowData, nowTime))  # 报告打开路径
    reportpath = report_path + r'/{}/{}'.format(nowData, nowTime)
    log.logger.info('报告文件：：' + reportpath)

    # Casepath = os.path.join(path, r"test_case/{}.py".format(case_name))  # 测试集合路径
    Casepath = test_case_path + r'/{}.py'.format(case_name)

    log.logger.info('测试用例地址：' + Casepath)

    # os.system('rm -rf {}/report/'.format(path))


    pytest.main([Casepath, "-s", "--alluredir", tempath])  # 运行 test_case下所有测试用例
    os.system(f'allure generate {tempath} -o {reportpath} -clean')
    os.system("allure open {} -h 0.0.0.0 -p 65535 &".format(reportpath))

if __name__ == '__main__':
    generate_report('test_dame')
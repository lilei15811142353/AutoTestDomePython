# -- coding: utf-8 --**

#encoding:utf-8
import os
import sys
import random
from commons.operationProcess import *
from commons.larkRobotMsg import *
from commons.getOutterIP import *
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


from flask import Flask,request
from commons.generate_report import *

app = Flask(__name__)
@app.route("/allProcess",methods=['GET'])
def run_testCase():
    case_name = request.args.get('case_name')

    while run(65535)['code'] == 200:
        run(65535)

    generate_report(case_name)

    larkMsg = '{}脚本运行完成，测试报告地址：http://{}:65535'.format(case_name,getOutterIP())
    larkRobotSend(larkMsg)

    msg = {
        "code":200,
        "msg":"larkMsg"
    }
    return msg


# app = Flask(__name__)
# @app.route("/Choosedish",methods=['GET'])
# def Choosedish():
#     listDish = ["鱼香肉丝","宫保鸡丁","可乐鸡翅","包子","水饺"]
#     random_element = random.choice(listDish)
#     # random_element = ran
#     msg = {
#         "code":200,
#         "dish":random_element
#     }
#     return msg


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=7666,debug=True)
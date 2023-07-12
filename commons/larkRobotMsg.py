#coding=utf-8
import os
import sys
from commons.editorFile import *
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from commons.apiRequest import *
import json
from commons import dirTool

'''
向飞书群发送消息
'''
apiurl = read_yaml_new(dirTool.config_path, 'config.yaml')['LarkRobot']['path']

# apiurl = read_yaml(os.getcwd(),'configs','config.yaml')['LarkRobot']['path']

def larkRobotSend(text):
    headers = {'Content-Type': 'application/json;charset=utf-8'}

    json_text = {
        "msg_type": "text",
        "content": {
            "msg": "zeppelin0.9告警通知",
            "text": text
        }
    }

    res = requ(headers).post(url=apiurl,dataParams=json.dumps(json_text))
    log.logger.info('发送飞书消息。返回结果：' + str(res))


if __name__ == '__main__':
    larkRobotSend('{}脚本运行完成，测试报告地址：http://{}:65535')
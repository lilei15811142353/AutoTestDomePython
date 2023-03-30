import requests,json
import urllib3

from commons.logconf import run_log as logger
from commons import log

class requ():
    def __init__(self,headers):
        self.headers = headers

    def get(self, url):  # get消息
        urllib3.disable_warnings()
        log.logger.info('请求URL：' + url)
        log.logger.info('请求信息头：' + str(self.headers))
        try:
            r = requests.get(url,params=None,verify=False,headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            log.logger.info('返回参数:' + str(json_response))
            return json_response
        except Exception as e:
            logger.info('get请求出错，出错原因:%s' % e)

    def post(self, url=None,jsonParams=None,dataParams=None):  # post消息
        urllib3.disable_warnings()
        if jsonParams != None:
            log.logger.info('请求参数：' + str(jsonParams))
        else:
            log.logger.info('请求参数：' + str(dataParams))

        if self.headers != None:
            log.logger.info('请求信息头：' + str(self.headers))
        else:
            pass
        try:
            r = requests.post(url, json=jsonParams,data=dataParams,headers=self.headers,verify=False)
            json_response = json.loads(r.text)
            log.logger.info('返回参数:' + str(json_response))
            return json_response
        except Exception as e:
            logger.info('post请求出错，出错原因:%s' % e)


    def postfile(self,url=None,jsonParams=None,dataParams=None,file=None):
        urllib3.disable_warnings()
        if jsonParams != None:
            log.logger.info('请求参数：' + str(jsonParams))
        else:
            log.logger.info('请求参数：' + str(dataParams))

        if self.headers != None:
            log.logger.info('请求信息头：' + str(self.headers))
        else:
            pass
        try:
            r = requests.post(url, json=jsonParams,data=dataParams,files=file,headers=self.headers,verify=False)
            json_response = json.loads(r.text)
            return json_response
        except Exception as e:
            logger.info('post请求出错，出错原因:%s' % e)
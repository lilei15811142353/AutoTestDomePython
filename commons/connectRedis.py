#encoding:utf-8
import os
import sys

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('./')
import redis
from commons import log
from commons.editorFile import read_yaml
import socket
socket.gethostname()

class conncetRedis:
    def __init__(self,db):
        self.db = db
        self.conn = read_yaml()['redis']
        self.conn['db'] = db
        try:
            self.connection = redis.ConnectionPool(**self.conn)
            log.logger.info('获取Reids连接池，链接信息:' + str(self.conn))
            self.res = redis.StrictRedis(connection_pool=self.connection)
            log.logger.info('连接成功：' + str(self.res))
        except Exception as e:
            log.logger.error('获取Redis连接池异常，程序退出：' + str(e))
            sys.exit(0)

    def getKeys(self,key):
        try:
            result = self.res.get(key)
            log.logger.info('查询redis数据:' + str(result))
            return result
        except Exception as e:
            log.logger.info('查询出错，出错原因:' + e)
            sys.exit(0)

    def setKeys(self,key,value):
        try:
            self.res.set(key,value)
            log.logger.info('写入数据成功')
        except Exception as e:
            log.logger.error("写入数据失败，失败原因:" + e)
            sys.exit(0)

    def delKeys(self,key):
        try:
            self.res.delete(key)
        except Exception as e:
            log.logger.error('删除数据失败，失败原因：' + e)
            sys.exit(0)


if __name__ == '__main__':
    a = conncetRedis(db=10).getKeys('pets:string_login_token_8E015CE53CE9B8D7_190')
    print(a)
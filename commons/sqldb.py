#coding=utf-8
import os
import sys
from commons.editorFile import *
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pymysql
import pymysql.cursors
from commons import log
from commons import dirTool


class mysqldb:
    def __init__(self):
        # self.conn = config.hhdb
        self.conn = read_yaml_new(dirTool.config_path,'config.yaml')['database']
# 查询sql
    def selectsql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = con.cursor()
        try:
            cursor.execute(sql)
            data = cursor.fetchall()
            log.logger.info('【SQL】：' + sql)
            log.logger.info('total ：' + str(len(data)))
            log.logger.info("查询结果：" + str(data))
            return data
        except Exception as e:
            log.logger.info("sql异常,错误原因：" + e)
        finally:
            cursor.close()
            conn.close()


# 更新sql 须慎用，后面必须加where条件
    def updatesql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = conn.cursor()
        # cursor.execute(sql)
        # conn.commit()
        try:
            res = cursor.execute(sql)
            log.logger.info('【SQL】：' + sql)
            log.logger.info('total ：' + str(res))
            conn.commit()
        except Exception as e:
            conn.rollback() # 发生错误时回滚
            log.logger.error("sql异常,错误原因：" + e)
        finally:
            cursor.close()  # 关闭游标操作
            conn.close()  # 关闭数据库连接
# 插入sql
    def insertsql(self, sql):
        conn = pymysql.connect(**self.conn)
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception as e:
            log.logger.info("sql异常,错误原因：" + e)
        finally:
            cursor.close()
            conn.close()

# delete 须慎用，后面必须加where条件
    def deletesql(self, sql):
        conn = pymysql.connect(**self.conn)
        cursor = conn.cursor()
        try:
            cursor.execute(sql)
            log.logger.info(sql)
            conn.commit()
        except Exception as e:
            conn.rollback()  # 发生错误时回滚
            log.logger.error("sql异常,错误原因：" + e)
        finally:
            cursor.close()  # 关闭游标操作
            conn.close()   # 关闭数据库连接
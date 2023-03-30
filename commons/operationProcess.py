import subprocess
import os
from commons.log import logger

def getPid(port):
    """获取进程pid"""
    try:
        back = subprocess.Popen("""lsof -i:%s | awk 'NR==2{print $2}'""" % (port), shell=True, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE).communicate()
        data = back[0].decode().split('\n')
    except Exception as e:
        logger.info('error:', e)
        data = []
    logger.info('端口对应的pid:{}'.format(data))
    return data


def killPid(pid):
    """杀死进程"""
    cmd = "kill -s 9 {}".format(pid)
    logger.info(cmd)
    result = os.system(cmd)
    if result == 0:
        logger.info("kill {} success".format(pid))
    else:
        logger.info("kill {} error".format(pid))


def run(port):
    data = getPid(port)
    pid = data[0]
    logger.info('pid数量:' + str(len(pid)))
    logger.info('pid:' + pid)
    if len(pid) > 0:
        killPid(pid)
        msg = {
            "code":200,
            "msg":'杀进程成功'
        }
    else:
        logger.info('未查到端口-{}进程:'.format(port))
        msg = {
            "code":1,
            "msg":'未查到端口-{}进程:'.format(port)
        }
    return msg

if __name__ == '__main__':
    run(65535)
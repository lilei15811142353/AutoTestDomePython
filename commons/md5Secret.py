import hashlib
from commons import log

def md5Secret(strData):
    log.logger.info('加密前字符串：' + strData)
    md5Str = hashlib.md5()
    md5Str.update(strData.encode('UTF-8'))
    log.logger.info('加密后字符串:' + md5Str.hexdigest())
    return md5Str.hexdigest()


def signMd5(**kwargs):
    strSign = 'sys=' + kwargs['sys'] + '&timestamp=' + str(kwargs['timestamp']) + '&token=' + kwargs['token'] + '&version=' + kwargs['version'] + kwargs['appKey']
    sign = md5Secret(strSign)
    return sign
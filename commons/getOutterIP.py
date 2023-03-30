import requests
import re

def getOutterIP():
    ip = ''
    try:
        res = requests.get('https://myip.ipip.net', timeout=5).text
        ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', res)
        ip = ip[0] if ip else ''
    except:
        pass
    return ip
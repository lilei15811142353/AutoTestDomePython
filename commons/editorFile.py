import sys
import os
import yaml
import time
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


#读取config.yaml配置文件
def read_yaml(proj_path,filePathName,fileName):
    yaml_path_read = os.path.join(proj_path, filePathName)
    yamlname_read = os.path.join(yaml_path_read, fileName)
    with open(yamlname_read,'r',encoding='utf-8') as file:
        data = file.read()
        result = yaml.load(data,Loader=yaml.FullLoader)
        return result

#写入yaml测试结果
def write_yamlFile(proj_path,filePathName,fileName,dictData):
    yaml_path_read = os.path.join(proj_path, filePathName)
    yaml_path_write = os.path.join(yaml_path_read,fileName)
    with open(yaml_path_write, 'w', encoding='utf-8') as file:
        yaml.dump(dictData, file)
        file.close()

def write_txt(proj_path,url,requestData,reponseData):
    txtRes  = '\n\n接口地址 ：' + str(url) + '\n请求参数 ：' + str(requestData) + '\n返回参数 ：' + str(reponseData)

    txtname = os.path.join(proj_path,'测试结果.txt')
    with open(txtname,'a',encoding='utf-8') as file:
        file.write(txtRes)
    file.close()

#更新yaml测试数据
def update_yaml(proj_path,filePathName,fileName,key1=None,key2=None,key3=None,value=None):
    yaml_path_read = os.path.join(proj_path, filePathName)
    yamlname_read = os.path.join(yaml_path_read, fileName)
    with open(yamlname_read,'r',encoding='utf-8') as f:
        file_data = f.read()
        data = yaml.safe_load(file_data)

    if key3 == None:
        if key2 == None:
            data[key1]=value
        else:
            data[key1][key2]=value
    else:
        data[key1][key2][key3]=value

    with open(yamlname_read, 'w', encoding='utf-8') as f:
        yaml.safe_dump(data, f)
        f.close()

def read_yaml_new(filePathName,fileName):
    yamlname_read = os.path.join(filePathName, fileName)
    with open(yamlname_read,'r',encoding='utf-8') as file:
        data = file.read()
        result = yaml.load(data,Loader=yaml.FullLoader)
        return result
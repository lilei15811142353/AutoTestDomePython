#encoding:utf-8
import pytest

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
sys.path.append('/')
from commons.editorFile import *
from commons import sqldb
from assertpy import assert_that
import allure
from commons.md5Secret import *
from commons.apiRequest import *
from commons.dirTool import *

class Test_pet_case:
    def setup_method(self):
        self.headers = read_yaml_new(config_path,'config.yaml')['headers']
        self.apiurl = read_yaml_new(config_path,'config.yaml')['apiurl']['url']


        # self.headers = read_yaml(root_path,'./configs', 'config.yaml')['headers']
        # self.apiurl = read_yaml(root_path,'configs', 'config.yaml')['apiurl']['url']


    # @pytest.fixture()
    # def sqlParms(self):
    #
    #     userId = sqldb.mysqldb().selectsql \
    #         ("sqlParams")[0][0]
    #     return userId


    @allure.story('执行用例')
    @allure.title('执行用例')
    @pytest.mark.run(order=1)
    # @pytest.mark.parametrize('path',[read_yaml(os.getcwd(),'apiData', 'testData.yaml')['updataUserInfo']['path']])
    # @pytest.mark.parametrize('reqData',[read_yaml(os.getcwd(),'apiData','testData.yaml')['updataUserInfo']['reqData']])
    @pytest.mark.parametrize('path',[read_yaml_new(data_path,'testData.yaml')['updataUserInfo']['path']])
    @pytest.mark.parametrize('reqData', [read_yaml_new(data_path,'testData.yaml')['updataUserInfo']['reqData']])
    def test_creatPet(self,path,reqData):
        # log.logger.info("tel:" + str(dict(reqData)['tel']))
        url = self.apiurl + path + "?tel=" + str(dict(reqData)['tel'])
        resMsg = requ(self.headers).get(url=url)
        log.logger.info('------------TEST RESULT-------------')
        log.logger.info('reponse_data:{}'.format(resMsg))
        assert_that(resMsg['code']).is_equal_to(1)
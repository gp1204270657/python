#coding=utf-8
import sys
import os
import json
import HTMLTestRunner
import unittest
from unittest import mock 
base_path=os.getcwd()
sys.path.append(base_path)
from Base.base_requests import request 


def get_value(key):
    data=read_json()
    return data[key]


def read_json():
    with open(base_path+"/Config/user_data.json") as f:
        data=json.load(f)
    return data

class Interface(unittest.TestCase):
    def test_face(self):
        url="https://www.baidu.com"
        data={                      
            "username":"111",
            "password":"222"
            }
        '''
        mock在项目中的运用
        '''
        mock_method=mock.Mock(return_value=get_value("api/beta"))
        request.run_main=mock_method
        res=request.run_main("get",url,data)
        self.assertEqual(res['errorCode'],1000)

    def test_face_02(self):
        url="https://www.baidu.com"
        data={                      
            "username":"111",
            "password":"222"
            }
        '''
        mock在项目中的运用
        '''
        mock_method=mock.Mock(return_value=get_value("api/beta"))
        request.run_main=mock_method
        res=request.run_main("get",url,data)
        self.assertEqual(res['errorCode'],1001)

if __name__ == "__main__":
    suite=unittest.TestSuite()
    suite.addTest(Interface("test_face"))
    suite.addTest(Interface("test_face_02"))
    file_path=base_path+"/Report/result.html"
    '''
    生成测试报告
    '''
    with open(file_path,"wb") as f:
        runner=HTMLTestRunner.HTMLTestRunner(stream=f,title="这是测试标题",description="这个是啥")
        runner.run(suite)
    f.close()
    
   
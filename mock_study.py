#coding=utf-8
from unittest import mock
import requests,unittest,json

def post_request(url,data):
    res=requests.post(url,data).json()
    return res


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("case开始运行")
    def tearDown(self):
        print("case结束运行")
    def test_login(self):
        url="https://www.baidu.com"
        data={
            "username":"11111"
        }
        #通过Mock可以直接进行数据比对，不需要请求，降低开发等待时间
        res=mock.Mock(return_value=data)
        self.assertEqual("2222",res())

    
if __name__ == "__main__":
    unittest.main()

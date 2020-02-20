#coding=utf-8
import sys
import os
base_path=os.getcwd()
sys.path.append(base_path)
import requests,unittest
from Base.base_requests import request

url="https://www.baidu.com"
data={
    "username":"11111",
    "password":"22222"

}
class TestCase01(unittest.TestCase):
 
    def setUp(self):
        print("case开始执行")

    def tearDown(self):
        print("case结束执行")
    @classmethod
    def setUpClass(cls):
        print("case类开始执行")
    @classmethod
    def tearDownClass(cls):
        print("case类结束执行")

    @unittest.skip("这个case不行执行")
    def test01(self):
        print("case01")
        data1={
            "username":"11111"
        }
        self.assertDictEqual(data1,data,msg="二个不相等")
        
    def test02(self):
        print("case02")
        data2={
        "username":"11111",
        "password":"22222"
        }
        self.assertDictEqual(data2,data,msg="二个不相等")

    def test03(self):
        flag=True
        self.assertFalse(flag,msg="不为false")
    def test04(self):
        flag=False
        self.assertTrue(flag)
    def test05(self):
        flag="111"
        flag1="222"
        self.assertEqual(flag,flag1)
    def test06(self):
        res=request.run_main("get",url,data)
        print(res)
        return res


if __name__ == "__main__":
    unittest.main()
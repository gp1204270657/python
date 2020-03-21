#coding=utf-8
import requests
import sys,os
import json
base_path=os.getcwd()
sys.path.append(base_path)
from Util.handle_init import handle_ini
# url="https://www.baidu.com"
# data={
#     "username":"11111",
#     "password":"22222"

# }
class BaseRequests:

    def send_get(self,url,data):
        res=requests.get(url=url,params=data)
        return res

    def send_post(self,url,data):
        res=requests.post(url=url,data=data)
        return res
    
    def run_main(self,method,url,data):

        path_url=handle_ini.get_value('server','host')
        if 'http' not in url:
            url=path_url+url
        if method=="get":
            res=self.send_get(url,data).text
        else:
            res=self.send_post(url,data).text
        try:
            res=json.loads(res)
        except:
            print("这是一个test")
        return res

request=BaseRequests()
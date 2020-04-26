#coding=utf-8
import requests
import sys,os
import json
from Util.handle_cookie import write_valuse
base_path=os.getcwd()
sys.path.append(base_path)
from Util.handle_init import handle_ini
# url="https://www.baidu.com"
# data={
#     "username":"11111",
#     "password":"22222"

# }
class BaseRequests:

    def send_get(self,url,data,cookie=None,get_cookie=None,is_header=None):

        respones=requests.get(url=url,params=data,cookies=cookie,headers=is_header)
        if get_cookie!=None:
            cookie_valus_jar=respones.cookies
            cookie_values=requests.utils.dict_from_cookiejar(cookie_valus_jar)
            write_valuse(cookie_values,get_cookie["is_cookie"])
        res=respones.text
        return res

    def send_post(self,url,data,cookie=None,get_cookie=None,is_header=None):
        respones=requests.post(url=url,params=data,cookies=cookie,headers=is_header)
        if get_cookie!=None:
            cookie_valus_jar=respones.cookies
            cookie_values=requests.utils.dict_from_cookiejar(cookie_valus_jar)
            write_valuse(cookie_values,get_cookie["is_cookie"])
        
        res=respones.text
        return res
    
    def run_main(self,method,url,data,cookie=None,get_cookie=None,is_header=None):

        path_url=handle_ini.get_value('server','host')
        if 'http' not in url:
            url=path_url+url
        if method=="get":
            res=self.send_get(url,data,cookie,get_cookie,is_header)
        else:
            res=self.send_post(url,data,cookie,get_cookie,is_header)
        try:
            res=json.loads(res)
        except:
            print("这是一个test")
        return res

request=BaseRequests()
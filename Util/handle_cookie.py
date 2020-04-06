#coding=utf-8
import sys,os
import openpyxl
import json
base_path=os.getcwd()
sys.path.append(base_path)

from Util.handle_json import read_json,write_Cookie

def get_cookid_valus(cookie_key):
    """读取COOKie"""
    data=read_json("/Config/cookie.json")
    return data[cookie_key]
  


def write_valuse(data,cookie_key):
    """写入cookie"""
    data1=read_json("/Config/cookie.json")
    data1[cookie_key]=data
    write_Cookie(data1)




if __name__ == "__main__":
    data={
        "aaa2":"1111"
    }
    print(write_valuse(data,"web"))
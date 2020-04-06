#coding=utf-8
import sys,os
import openpyxl
import json
base_path=os.getcwd()
sys.path.append(base_path)


def get_value(key,file_name=None):
    data=read_json(file_name)
    return data.get(key)


def read_json(file_name=None):
    if file_name==None:
        file_path=base_path+"/Config/user_data.json"
    else:
        file_path=base_path+file_name
    with open(file_path,encoding="utf-8") as f:
        data=json.load(f)
    return data

def write_Cookie(data):
    #转换成字典格式
    data=json.dumps(data)
    with open(base_path+"/Config/cookie.json",'w',encoding="utf-8") as f:
        f.write(data)
    
if __name__ == "__main__":
    data={
        "aaa":"bbb"
    }
    write_Cookie(data)
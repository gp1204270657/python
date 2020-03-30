#coding=utf-8
import sys,os
import openpyxl
base_path=os.getcwd()
sys.path.append(base_path)
from Util.handle_json import get_value
# date=get_value("api3/beta4","/Config/code_message.json")
# print(date)


def handle_result(url,code):
    date=get_value(url,"/python/Config/code_message.json")
    if date!=None:
        for i in date:
            message=i.get(str(code))
            if message:
                return message
    return None


if __name__ == "__main__":
    print(handle_result("api3/beta5","1002"))
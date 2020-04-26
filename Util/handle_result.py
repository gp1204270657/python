#coding=utf-8
import sys,os
import openpyxl
from deepdiff import DeepDiff
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


def get_result_json(url,status):
    date=get_value(url,"/Config/result.json")
    if date!=None:
        for i in date:
            message=i.get(status)
            if message:
                return message
    return None




def handle_result_json(dict1,dict2):
    #通过deepdeef比对二个方法,校验格式
    if isinstance(dict1,dict) and isinstance(dict2,dict):

        cmp_dict=DeepDiff(dict1,dict2,ignore_order=True).to_dict()
        if cmp_dict.get("dictionary_item_added"):
            return True
        else:
            return False
    return False

     


if __name__ == "__main__":
    # print(handle_result("api3/beta5","1002"))
    print(get_result_json("api/beta3","moou"))
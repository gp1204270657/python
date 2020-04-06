#coding=utf-8
import sys,os
import openpyxl
import unittest
base_path=os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data
from Base.base_requests import request
from Util.handle_result import handle_result
from Util.handle_result import handle_result_json,get_result_json

class RunMain():
    def run_case(self):
        row=excel_data.get_row()
        
        for i in range(row):
            data=excel_data.get_row_value(i+2)
            is_run=data[2]
            if is_run=='yes':
                method=data[5]
                url=data[4]
                data1=data[6]
                exthed_method=data[8]
                exthed_result=data[9]
                res=request.run_main(method,url,data1)
                print(res)
                print(url)
                
                if exthed_method=='mec':
                    code="1003"
                    # message=res['errorCodeMes']
                    message="用户名错误"
                    config_message=handle_result(url,code)
                    if message==config_message:
                        print("测试通过")
                    else:
                        print("测试失败")
                if exthed_method=='errorcode':
                    code="1006"
                    if exthed_result==code:
                        print("测试通过")
                    else:
                        print("测试失败")
                if exthed_method=="json":
                    code=res['errorCode']
                    # print("code=====",code)
                    if code=="10067":
                        status="error"
                    else:
                        status="succes"
                    excute_result=get_result_json(url,status)
                    result=handle_result_json(res,excute_result)
                    if result:
                        print("case执行成功")
                    else:
                        print("case执行失败")
                    


                



if __name__ == "__main__":
    run=RunMain()
    run.run_case()
#coding=utf-8
import sys,os
import json
import openpyxl
import unittest
base_path=os.getcwd()
sys.path.append(base_path)
from Util.handle_excel import excel_data
from Base.base_requests import request
from Util.handle_result import handle_result
from Util.handle_result import handle_result_json,get_result_json
from Util.handle_cookie import get_cookid_valus,write_valuse
from Util.handle_header import get_header

class RunMain():
    def run_case(self):
        row=excel_data.get_row()
        
        for i in range(row):
            cookie=None
            get_cookie=None
            data=excel_data.get_row_value(i+2)
            is_run=data[2]
            if is_run=='yes':
                method=data[5]
                url=data[4]
                data1=data[6]
                header=data[13]
                exthed_method=data[8]
                exthed_result=data[9]
                cookie_mother=data[7]
                if cookie_mother=="yes":
                    cookie=get_cookid_valus("app")
                
                if cookie_mother=="write":
                    get_cookie={"is_cookie":"app"}
                if header=="yes":
                    is_header=get_header()
                res=request.run_main(method,url,data1,cookie,get_cookie,is_header)
              
                                
                if exthed_method=='mec':
                    code="1003"
                    # message=res['errorCodeMes']
                    message="用户名错误"
                    config_message=handle_result(url,code)
                    if message==config_message:
                        excel_data.excel_write_Data(i+2,11,"通过")
                        print("测试通过")
                    else:
                        excel_data.excel_write_Data(i+2,11,"失败")
                        excel_data.excel_write_Data(i+2,12,json.dumps(res))
                        print("测试失败")
                if exthed_method=='errorcode':
                    code="1006"
                    if exthed_result==code:
                        excel_data.excel_write_Data(i+2,11,"通过")
                        print("测试通过")
                    else:
                        excel_data.excel_write_Data(i+2,11,"失败")
                        excel_data.excel_write_Data(i+2,12,json.dumps(res))
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
                        excel_data.excel_write_Data(i+2,11,"通过")
                    else:
                        excel_data.excel_write_Data(i+2,11,"失败")
                        excel_data.excel_write_Data(i+2,12,json.dumps(res))
                    


                



if __name__ == "__main__":
    run=RunMain()
    run.run_case()
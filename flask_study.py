 #coding=utf-8
from flask import Flask
from flask import request
import json
app=Flask(__name__)

@app.route('/')
def Home():
    data=json.dumps({
        "username":"musisi",
        "password":"123123"
    })
    return data

'''
创建get请求地址
'''
@app.route('/user/login',methods=['GET'])
def get_login():
     username=request.args.get("username")
     password=request.args.get("password")
     if username and password:
        data=json.dumps({
            "username":username,
            "password":password,
            "code":200,
            "message":"登录成功"
        })
     else:
         data=json.dumps({
             "message":"参数错误"
             })
        
     return data

@app.route('/post/login',methods=['POST'])
def post_login():
    #获取request的请求方式
    reques_methord=request.method
    if reques_methord=='POST':
         username=request.form.get("username")
         password=request.form.get("password")
         data=json.dumps({
            "username":username,
            "password":password,
            "code":200,
            "message":"登录成功"
        })
     else:
         data=json.dumps({
             "message":"参数错误"
             })
    return data 
    

if __name__ == "__main__":
    app.run()  
   
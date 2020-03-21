#coding=utf-8
import sys,os
import openpyxl
import configparser
base_path=os.getcwd()
sys.path.append(base_path)

file_path=base_path+"/Config/server.ini"
#读取配置文件的对象
cf=configparser.ConfigParser()
cf.read(file_path)
data=cf.get('server','host')
print(data)

class HandleInit:

    def load_init(self):
        file_path=base_path+"/Config/server.ini"
        #读取配置文件的对象
        cf=configparser.ConfigParser()
        cf.read(file_path)
        return cf

    def get_value(self,section,key):
        '''
        获取配置对象具体某一项的值
        '''
        cf=self.load_init()
        data=cf.get(section,key)
        return data
handle_ini=HandleInit()

    



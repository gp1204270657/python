from DBUtils.PooledDB import PooledDB
import pymysql,sys,os

try:
    pooldb=PooledDB(pymysql,10,host="localhost",user="root",passwd="123123",db="vega")
    # pool=pooldb.connection()
        
except Exception as e:
    print(e)
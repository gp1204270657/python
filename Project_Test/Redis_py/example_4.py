#coding=utf-8
from Project_Test.Redis_py.redis_db import pool
import redis

con=redis.Redis(
    connection_pool=pool
)
try:
    #创建一个集合
    con.sadd("employee",8001,8002,8003)
    con.srem("employee",8002)
    result=con.smembers("employee")
    for one in result:
        print(one.decode("utf-8"))
    #创建一个有序集合
    con.zadd("keyword",{"马云":0,"张朝阳":0,"刘强东":0})
    con.zincrby("keyword",10,"刘强东")
    result=con.zrevrange("keyword",0,-1)
    for one in result:
        print(one.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con
#coding=utf-8
from Project_Test.Redis_py.redis_db import pool
import redis
#创建连接池
con=redis.Redis(
    connection_pool=pool
)
try:
    con.delete("country","city")
    #重新设置字典
    con.mset({"country":"德国","city":"难受"})
    result=con.mget("country","city")
    #循环遍历获取
    for one in result:
        print(one.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    #强制回收链接池
    del con




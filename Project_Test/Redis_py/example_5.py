from  Project_Test.Redis_py.redis_db import pool
import redis

con=redis.Redis(
    connection_pool=pool
)

try:
    #创建hash函数
    con.hmset("9527",{"name":"scott","sex":"male","age":"26"})
    con.hset("9527","city","纽约")
    con.hdel("9527","sex")
    result=con.hexists("9527","age")
    print(result)
    result1=con.hgetall("9527")
    for one in result1:
        print(one.decode("utf-8"),result1[one].decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con
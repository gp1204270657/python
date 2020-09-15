from Project_Test.Redis_py.redis_db import pool
import redis
import random

con=redis.Redis(
    connection_pool=pool
)

try:
    con.delete("ballot")
    con.zadd("ballot",{"马云":0,"马化腾":0,"刘强东":0})
    names=["马云","马化腾","刘强东"]
    for i in range(0,300):
        num=random.randint(0,2)
        name=names[num]
        con.zincrby("ballot",1,name)
    result=con.zrevrange("ballot",0,-1,"WITHSCORES")
    for one in result:
        print(one[0].decode("utf-8"),int(one[1]))
except Exception as e:
    print(e)
finally:
    del con
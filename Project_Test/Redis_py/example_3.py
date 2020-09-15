from Project_Test.Redis_py.redis_db import pool
import redis

con=redis.Redis(
    connection_pool=pool
)
try:
    #创建一个列表
    con.rpush("dname","董事会","技术部","水杯")
    con.lpop("dname")
    result=con.lrange("dname",0,-1)
    for one in result:
        print(one.decode("utf-8"))
except Exception as e:
    print(e)
finally:
    del con
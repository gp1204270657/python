from Project_Test.Redis_py.redis_db import pool
import redis

con=redis.Redis(
    connection_pool=pool
)
try:
    #事务的调用
    pipline=con.pipeline()
    #监视事务
    pipline.watch("9527")
    #开启事务
    pipline.multi()
    pipline.hset("9527","name","jack")
    pipline.hset("9527","sex","male")
        #提交事务
    pipline.execute()
except Exception as e:
    print(e)
finally:
    if "pipline" in dir():
        pipline.reset()
    del con
from Project_Test.Redis_py.redis_db import pool
import redis
import time
con=redis.Redis(
    connection_pool=pool
)
con.set("country","英国")
con.set("city","上海")
#设置5s过期
con.expire("country",5)
time.sleep(6)
cty=con.get("country").decode("utf-8")
print(cty)
del con

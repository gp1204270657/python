#coding=utf-8
import redis
#创建一个连接
# r=redis.Redis(
#     host="localhost",
#     port=6379,
#     password="123456",
#     db=0
# )

#创建通过连接池来连接
try:
    pool = redis.ConnectionPool(
        host="localhost",
        port=6379,
        db=0,
        max_connections=10
    )
except Exception as e:
    print(e)

    

from Project_Test.Redis_py.redis_db import pool
import redis

con=redis.Redis(
    connection_pool=pool
)

try:
    file=open("score.txt","r",encoding="utf-8")
    data=file.read().splitlines()
    for one in data:
        temp=one.split(",")
        sid=temp[0]
        name=temp[1]
        calssno=temp[2]
        score_1=int(temp[3])
        score_2 = int(temp[4])
        score_3 = int(temp[5])
        if score_1>=80 and score_2>=80 and score_3>=80:
            con.hmset(sid,{"name":name,"classno":calssno,"score1":score_1,"score2":score_2,"score3":score_3})

    print("执行成功")

except Exception as e:
    print(e)
finally:
    del con
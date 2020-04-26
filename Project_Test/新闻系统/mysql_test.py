import pymysql
from DBUtils.PooledDB import PooledDB
#连接数据库
#查询语句
# con=pymysql.connect("localhost","root","123123","test")
# #创建游标
# cursor=con.cursor()
# sql="select empno,ename,job from t_emp"
# #运行sql语句
# cursor.execute(sql)
# #取出数据
# for one in cursor:
#     print(one[0],one[1],one[2])

# con.close()


"""
异常处理
"""
#增加语句
# try:
#     con=pymysql.connect("localhost","root","123123","test")
#     curson=con.cursor()
#     sql="insert into t_emp(empno,ename,job,mgr,hiredate,sal,comm,deptno) values (%s,%s,%s,%s,%s,%s,%s,%s)";
#     curson.execute(sql,(9908,"zhangsan","haha",None,"1988-12-13",2000,None,10))
#     #提交事务
#     con.commit()
# except Exception as e:
#     #异常则回滚
#     if "con" in dir():
#         con.rollback()
#     print(e)

# finally:
#     if "con" in dir():
#         con.close()
"""
数据库连接池的实现
"""
#更新数据
# try:

#     pool = PooledDB(pymysql, 5, host="localhost", user='root',
#                 passwd='123123', db='test')
#     con=pool.connection()
#     curson=con.cursor()
#     sql="update t_emp set sal=sal+%s where deptno=%s";
#     curson.execute(sql,(200,20))
#     con.commit()    
# except Exception as e:
#     if "con" in dir():
#         con.rollback()
#     print(e)

#删除语句

try:
    pool=PooledDB(pymysql,5,host="localhost",user="root",passwd="123123",db="test")
    con=pool.connection()
    curson=con.cursor()
    sql="delete e,d from t_emp e join t_dept d on e.deptno=d.deptno where d.deptno=20 "
    curson.execute(sql)
    con.commit()
except Exception as e:
    if "con" in dir():
        con.rollback()
    print(e)



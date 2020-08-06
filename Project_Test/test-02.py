#coding=utf-8
# 导入pymysql模块
import pymysql
import datetime
import random


# 连接database
conn = pymysql.connect(host="10.0.34.104", user="ua_online_dataconvert",password="rk8PEjZzwX7t40JDL7",database="online_dataconvert",charset="utf8")
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()
# 定义要执行的SQL语句

for i in range(1):
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    num = random.randint(56000,89632)
    cid = random.randint(89000,99000)
    uid = random.randint(66666,77777)
    sql ='''
    INSERT INTO carrier_boutique_line VALUES
     (num, 'JP20200727190002', cid, '承运商评分二',
     uid, '小白', '13636561554', '螺纹钢',
      440100, '广州市', 440111, '白云区', 9527,
      '小白', 320500, '苏州市', 320508, '姑苏区', 1,
      1, '小白', time,
       '小白', time);
    '''
    # 执行SQL语句
    cursor.execute(sql)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
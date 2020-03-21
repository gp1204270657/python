#coding=utf-8
from datetime import datetime,date,time,timedelta
#1.创建自定义的时间
d=datetime(2020,3,14,20)
print(d)
t=date(2019,11,9)
print(t)
o=time(12,23,54)
print(o)

#2.时间日期与字符串之间的转换
#字符串转换为datetime对象
dr="2019-10-3 15:23:41"
dt=datetime.strptime(dr,"%Y-%m-%d %H:%M:%S")
print(dt)
#datetime对象转换为字符串
da=datetime.now()
da1=da.strftime("%Y-%m-%d %H:%M:%S")
print(da1)
#时间的加减法
n=datetime.now()
n1=n+timedelta(days=3,hours=4)
print(n1)
print("-----------------------")
#时间的减法

t1=datetime(2020,3,5)
t2=datetime(2020,2,29)
rest=t1-t2
print(rest.days)
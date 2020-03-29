import re

content="adjaskd1231fkjfUk23jfskdjk55324jkfdk34"
#编译成一个对象
patter=re.compile(r'\d+',re.I)
#findall 查找所有匹配的对象
res=patter.findall(content)
print(res)



#不编译对象直接查找
res1=re.findall(r'\d+',content,re.I)
print(res1)

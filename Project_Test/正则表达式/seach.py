import re

content="adjaskd1231fkjfUk23jfskdjk55324jkfdk34"
#编译成一个对象
patter=re.compile(r'\d+',re.I)
#seach 查找第一个匹配到的对象
res=patter.search(content)
print(res)


#不编译对象直接查找
res1=re.search(r'(\d+)',content,re.I)
print(res1)
#group是分组的概念
print(res1.group())
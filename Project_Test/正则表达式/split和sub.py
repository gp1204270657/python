import re

content='one1two2three3333four4five5'
p=re.compile('\d+')
#将匹配到的切割出来
rest=p.split(content)
print(rest)

#将匹配出来的结果用字符串替换掉
rest1=p.sub('@',content)
print(rest1)

#将匹配出来的结果用正则表达式替换,位置改变
s2='hello world'
p1=re.compile(r'(\w+) (\w+)')
result=p1.sub(r'\2 \1',s2)
print(result)

#将匹配出来的结果用函数替换
def f(m):
    return m.group(2).upper()+m.group(1)
result_2=p1.sub(f,s2)
print(result_2)
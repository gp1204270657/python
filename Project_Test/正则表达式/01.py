import re

#将要匹配的返回为一个正则表达式的对象
patter=re.compile(r"hello",re.I)

#对其进行处理
rest=patter.match("hello ,world")
print(dir(rest))
print(rest.string)
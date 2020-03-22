#coding=utf-8
from functools import reduce
def get_reduce(l):

    #lambda是匿名函数
    #reduce是将里面二个元素相加得到的和，再与第三个数求和,返回结果是一个值
    rest=reduce(lambda m,n:m+n ,l)
    return rest

def get_20_resule(l):
    #计算阶乘
    rest=reduce(lambda m,n:m*n,l)
    return rest

if __name__ == "__main__":
    l=[1,2,3,4,5,6]
    rest=get_reduce(l)
    print(rest)
    list_str=range(1,21)
    print(list_str)
    rest_2=get_20_resule(list_str)
    print(rest_2)


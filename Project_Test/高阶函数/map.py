#coding=utf-8
def get_map(l):

    #lambda是匿名函数
    #map是将传入的函数依次作用到每一个传入的值，返回是一个列表
    rest=map(lambda n: n*n*n,l)
    return rest

if __name__ == "__main__":
    l=range(1,4)
    rest=get_map(l)
    print(list(rest))
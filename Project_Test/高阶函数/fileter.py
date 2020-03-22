#coding=utf-8
def get_num(l):

    #取奇数的值,lambda是匿名函数
    #fileter是一个过滤器，返回的是一个列表
    rest=filter(lambda n: n%2==0,l)
    return rest

if __name__ == "__main__":
    l=range(1,51)
    rest=get_num(l)
    print(list(rest))
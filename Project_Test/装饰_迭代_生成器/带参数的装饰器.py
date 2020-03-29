from functools import wraps

#带参数的 name
def log(name=None):
    def new_wapper(func):
        @wraps(func)#这个是将函数保留原来的属性好名字等内容__name__,__dic__
        #方法带参数时，需要在这个加上无限制个数的参数*args,*kwargs
        def wapper(*args,**kwargs):
            print("{0}开始执行。。。".format(name))
            res=func(*args,**kwargs)
            print(res)
            print("{0}结束执行".format(name))
            return res
        return wapper
    return new_wapper

#函数不带参数
@log("张三")
def hello():
    print("hello world")


#函数带参数的
@log("李四")
def add(a,b,*args,**kwargs):
    return a+b

if __name__ == "__main__":
    hello()
    add(1,2,5,6)
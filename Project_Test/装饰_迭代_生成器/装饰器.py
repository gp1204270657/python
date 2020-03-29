

def log(func):
    def wapper():
        print("开始执行。。。")
        func()
        print("结束执行")
    return wapper

def log_1(func):
    def wapper():
        print("start。。。")
        func()
        print("end...")
    return wapper
    
#调用装饰器的方法,可以多个调用
@log
@log_1
def hello():
    print("hello world")


if __name__ == "__main__":
    hello()
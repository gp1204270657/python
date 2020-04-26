import time
from multiprocessing import Process

def do_sth(name):
    """进程要做的事情"""
    print("传进来的名字是{0}".format(name))
    time.sleep(3)
    print("进程开始做的事")

#通过面向对象的方法是实现
class my_process(Process):
    def __init__(self,name,*args,**kwargs):
        self.my_name=name
        super().__init__(*args,**kwargs)


    def run(self):
        print("传进来的名字是{0}".format(self.my_name))
        time.sleep(3)
        print("进程开始做的事")



if __name__ == "__main__":
    # p=Process(target=do_sth,args=("my process",))
    my=my_process("class process")
    my.start()
    my.join()

    # p.start()
    # p.join()
from multiprocessing import Process,Queue
import time
import random


class Proces_write(Process):
    def __init__(self,q,*args,**kwargs):
        self.q=q
        super().__init__(*args,**kwargs)

    def run(self):
        ls=[
            "第一行的内容",
            "第二行的内容",
            "第三行的内容",
            "第四行的内容"
        ]
        for i in ls:
            print("写入的内容是{0}".format(i))
            self.q.put(i)
            time.sleep(random.randint(1,3))
            


class Proces_read(Process):

    def __init__(self,q,*args,**kwargs):
        self.q=q
        super().__init__(*args,**kwargs)

    def run(self):
        while True:
            context=self.q.get()
            print("读取的内容是{0}".format(context))

if __name__ == "__main__":
    #通过Queue二个之间来通信
    q=Queue()
    p=Proces_write(q)
    r=Proces_read(q)
    p.start()
    r.start()
    r.join()
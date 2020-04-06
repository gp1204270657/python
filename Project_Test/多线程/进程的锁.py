from multiprocessing import Process,Lock
import time ,random

class WriteProcess(Process):

    def __init__(self,file_name,num,lock,*args,**kwargs):
        self.file_name=file_name
        self.num=num
        self.lock=lock
        super().__init__(*args,**kwargs)

    def run(self):
        #写入数据的方法
        try:
            #也可通过 with.self.lock()方法来写
            self.lock.acquire()
            for i in range(5):
                #记录写入的内容
                content="现在写入的是{0}，id是{1}，进程的是{2} \n".format(self.name,self.pid,self.num)
                with open(self.file_name,"a+",encoding="utf-8") as f:
                    f.write(content)
                    time.sleep(random.randint(1,3))
                    print(content)
        finally:
            self.lock.release()
if __name__ == "__main__":
    file_name="test.txt"
    #调用进程的锁来一个一个的执行
    lock=Lock()
    for i in range(5):
        w=WriteProcess(file_name,i,lock)
        w.start()
        #此处不用join,因为用来就会启用完一个进程之后才会启用第二个进程
        # w.join()




        

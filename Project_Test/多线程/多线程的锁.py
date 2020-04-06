import threading
import time


#创建二个锁
my_lock=threading.Lock()
#同时锁住二次，不会造成死锁
you_lock=threading.RLock()
num=0
def change(n):
    #要调用全局的变量需要用到global关键字
    global num
    #调用锁的方法
    # print("start lock...")
    # #同时调用二个锁的话 ，会造成死锁
    # you_lock.acquire()
    # # my_lock.acquire()
    # print("lock one ")
    # you_lock.acquire()
    # # my_lock.acquire()
    # print("lock two")
    #可以使用with关键字来运用锁
    with my_lock:
        num=num+n
        time.sleep(2)
        num=num-n
        time.sleep(1)
        print("---N---->{0}------num----->{1}".format(n,num))
    # #将锁释放
    # you_lock.release()
    # you_lock.release()

class Therad_test(threading.Thread):

    def __init__(self,n1,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.n1=n1

    def run(self):
        for i in range(1000):
            change(self.n1)

if __name__ == "__main__":
    t1=Therad_test(5)
    t2=Therad_test(8)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("last num :{0}".format(num))

    
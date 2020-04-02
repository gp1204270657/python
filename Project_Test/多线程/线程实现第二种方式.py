import threading 
import time
#继承类
class test(threading.Thread):
    n=0
    #调用run方法来实现
    def run(self):
        while self.n<5:
            print(self.n)
            now_thread=threading.currentThread()
            print("now thread name：{0}".format(now_thread))
            time.sleep(1)
            self.n+=1

if __name__ == "__main__":
    t=test()
    now_thread=threading.currentThread()
    print("now thread name：{0}".format(now_thread))
    t.start()
    t.join()
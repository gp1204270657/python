import threading
import time

def loop():
    n=0
    while n<5:
        print(n)
        now_thread=threading.current_thread()
        print("loop thread name:{0}".format(now_thread))
        time.sleep(1)
        n+=1

def user_thread():
    #调用Threading模块的方法是实例化对象
    t=threading.Thread(target=loop,name="loop thread")
    #查看当前的线程的名称
    now_thread=threading.current_thread()
    print("now thread name:{0}".format(now_thread))
    t.start()
    t.join()

if __name__ == "__main__":
    user_thread()
    
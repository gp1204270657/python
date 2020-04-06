import time
import threading
from multiprocessing.dummy import Pool 
from concurrent.futures import ThreadPoolExecutor
def run(n):
    time.sleep(2)
    print(threading.current_thread().name,n)

def main():
    t1=time.time()
    for n in range(5):
        run(n)
    print(time.time()-t1)

#第一种方法使用线程池的方法
def main_user_pool():
    #创建一个线程池，数量为10
    t1=time.time()
    n_list=range(100)
    pool=Pool(10)
    pool.map(run,n_list)
    pool.close()
    pool.join()
    print(time.time()-t1)

#使用ThreadPoolExecutor来创建线程池
def user_executor():
    t1=time.time()
    n_list=range(100)
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(run,n_list)
    print(time.time()-t1)
    






if __name__ == "__main__":
    # main()
    # main_user_pool()
    user_executor()
    
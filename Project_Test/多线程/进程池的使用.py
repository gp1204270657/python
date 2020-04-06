from multiprocessing import current_process,Pool
import time,random


def run(file_name,num):
    """
    写入文件
    """
    with open(file_name,"a+",encoding="utf-8") as f:
        #获取当前的进程的信息
        now_process=current_process()
        content="{0}--{1}---{2}".format(now_process.name,now_process.pid,num)
        f.write(content)
        f.write("\n")
        time.sleep(random.randint(1,2))
        print(content)
    return "ok"


if __name__ == "__main__":
    file_name="text_pool.txt"
    pool=Pool(2)
    for i in range(10):
        #同步添加任务
        rest=pool.apply(run,args=(file_name,i))
        print("{0}>>>>>>{1}".format(rest,i))
    #关闭池子
    pool.close()
    pool.join()
        

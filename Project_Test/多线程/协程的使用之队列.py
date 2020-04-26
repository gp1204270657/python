import asyncio
import random

async def add(store,name):
    #写入一个文件
    for i in range(5):
        await asyncio.sleep(random.randint(1,3))
        await store.put(i)
        print("add one..{0},大小{1},名字{2}".format(i,store.qsize(),name))

async def reduce(store):
    #去掉一个数
    for i in range(10):
        rest=await store.get()
        print("reduce one...{0},大小{1}".format(i,store.qsize()))


if __name__ == "__main__":
    #创建一个队列
    store=asyncio.Queue(maxsize=5)
    a1=add(store,'a1')
    a2=add(store,'a2')
    r=reduce(store)
    #创建一个事件循环
    loop=asyncio.get_event_loop()
    #运行等待结束
    loop.run_until_complete(asyncio.gather(a1,a2,r))
    #关闭
    loop.close()

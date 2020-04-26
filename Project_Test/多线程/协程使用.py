import asyncio

#定义一个协程函数
async def do_sth(x):
    print("等待中。。。{0}".format(x))
    await asyncio.sleep(x)

#判断是否为协程函数
# print(asyncio.iscoroutinefunction(do_sth))

if __name__ == "__main__":
    cruute=do_sth(5)
    #获取事件的循环队列
    loop=asyncio.get_event_loop()
    #注册任务
    # task=loop.create_task(cruute)
    # print(task)
    #等待协程任务执行结束
    loop.run_until_complete(cruute)
    # print(task)

import asyncio

#定义一个协程函数
async def comput(x,y):
    print("正在计算{0}+{1}".format(x,y))
    await asyncio.sleep(3)
    return x+y

async def do_Sth(x,y):
    rest=await comput(x,y)
    print("计算结果为{0}".format(rest))
    return rest

if __name__ == "__main__":
    cone=do_Sth(2,3)
    #获取事件的循环队列
    loop=asyncio.get_event_loop()
    #注册任务
    # task=loop.create_task(cone)
    #等待任务执行完成
    loop.run_until_complete(cone)
    loop.close()

    


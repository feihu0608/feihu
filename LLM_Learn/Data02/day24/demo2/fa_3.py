"""
    协程函数并行执行的效果
    顶级任务退出以后 整个EventLoop都将结束
"""

import asyncio
import time

async def work(name,dealy):
    print(f"{name}任务开始执行了")
    await asyncio.sleep(dealy)
    print(f"{name}任务执行完毕了")
    return f"{name}任务的返回值"


async def main():
    print("======串行执行总耗时======")
    # 将work函数调用封装为任务 task 此时这个函数会立即执行
    asyncio.create_task(work("A",1))
    # 将work函数调用封装为任务 task 此时这个函数会立即执行
    asyncio.create_task(work("B",2))

    # 通过gather() 实现多个task对象的处理
    # results = await asyncio.gather(task_1,task_2)
    # print("所有函数的返回值：",results)



if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)




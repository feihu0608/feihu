"""
    协程函数串行执行的效果
"""

import asyncio
import time

async def work(name,dealy):
    print(f"{name}任务开始执行了")
    await asyncio.sleep(dealy)
    print(f"{name}任务执行完毕了")


async def main():
    print("======串行执行总耗时======")
    await work("A",1) # 这里相当于等待A任务执行完成
    await work("B",2) # 然后再执行B任务


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)




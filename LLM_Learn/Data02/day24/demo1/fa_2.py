"""
    协程函数 通过async 和 await 关键字实现 的
"""

import asyncio

async def hello():
    print('hello')
    await asyncio.sleep(1)  # 休眠1秒
    print('world')



if __name__ == '__main__':
    # 对于协程函数 直接调用不会执行 因为协程函数需要专门的角色来负责统一的调度分配执行权
    cor_obj = hello()
    print(cor_obj)  # __str__ 魔法函数 自我介绍
    print(type(cor_obj))

    asyncio.run(hello()) # 将当前函数加入到EventLoop队列





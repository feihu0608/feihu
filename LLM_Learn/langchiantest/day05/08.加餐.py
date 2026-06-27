# http就是我们平时发的网络请求（80）  https（ssl）网络会更稳定和安全（443）
# 是一个应用层协议（规矩，约定），基于底层tcp协议做的
import asyncio
# http我们要知道这个规范规矩，其实就是规定了，前后端之间在交互的时候，传递什么东西
# http就是报文：请求报文，响应报文
# 报文：行 头 空行 体 最终组成一个大的一坨字符串

# http的请求方式：
# GET‌：获取资源，数据附在 URL 后，可缓存、可收藏，适合查数据。******   查
# POST‌：提交数据到服务器，数据在请求体中，适合表单提交、文件上传。***** 增
# PUT‌：更新或替换指定资源，需传完整数据，多次执行结果一致。***** 改
# DELETE‌：删除指定资源，用于移除服务器上的数据。****** 删



# HEAD‌：只获取响应头信息，不返回内容，常用于检查资源是否存在。
# OPTIONS‌：查询服务器支持的请求方法，常用于跨域预检。
# PATCH‌：局部更新资源，只传需要修改的字段，节省带宽。
# TRACE‌：回显请求内容，用于调试和诊断，出于安全常被禁用。
# CONNECT‌：建立隧道连接，主要用于 HTTPS 代理场景。‌


# http的状态码
# 100  正在请求中，一般看不到
# 200  成功
# 300  重定向
# 400  前端有问题
# 500  服务器有（后端有问题）








# json
# json是一种数据格式 本质是一个字符串，前后端交互的时候数据都要以它为桥梁
# python当中就有json的序列化和反序列化相关的工具  json包
# 前端也有这个序列化和反序列的工具  stringfy
import json
# 直接把数据进行操作
# json.loads() 反序列化
# json.dumps() 序列化


dict1 = {
    'username':'zhangsan',
    "password":"123456"
}

dict_json = json.dumps(dict1)
print(dict_json,type(dict_json))


json_dict = json.loads(dict_json)
print(json_dict,type(json_dict))



# 操作json相关的文件
# json.load()
# json.dump()
dict2 = {
    'username':'lisi',
    "password":"123456"
}

# json.dump(dict2,open("dict2.json","w")) #把python对象序列化成json写入json文件
#
# result = json.load(open("dict2.json","r")) #把json文件当中的json数据反序列化后给你
# print(result,type(result))



# 协程
# 多进程和多线程是操作系统级别的调度

# 协程是程序员级别的调度  写代码的人自己写的逻辑  它的效率会更高
# 通过异步实现的  异步思想要么就是回调函数去做，要么就是事件循环
# 其实就是一个很大的死循环，事件循环我们可以理解为就是一个存储任务的容器，死循环就一直去监控容器当中的任务
# 一旦这个任务达到特定的状态，就做特定的事
# 不管是多进程还是多线程还是协程，其实最基本的功能就是解决阻塞
# 协程后期要么就是单协程任务（asyncio.run），要么就是多协程任务(asyncio.gather)



# async和await关键字的作用
# async方在函数前面，函数就变成异步函数，异步函数加括号调用的时候，结果一定是协程对象
# 此时，函数当中的代码并没有执行，当我们把这个协程对象扔到事件循环才有可能执行


# await
# 把当前协程任务的执行挂起，去事件循环找就绪状态的协程去执行

















# async def func():
#     import asyncio
#     # import time
#     print("我爱你杨幂")
#     await asyncio.sleep(2)
#     print("我爱你迪丽热巴")
#     return 100
#
# async def func2():
#     import asyncio
#     print("我爱你刘诗诗")
#     # import time
#     await asyncio.sleep(2)
#     print("我爱你刘亦菲")
#     return 200
#
#
# async def main():
#     # task1 = asyncio.create_task(func())
#     # task2 = asyncio.create_task(func2())
#     result = await asyncio.gather( func2(),func())
#     print(result)
#
#
# if __name__ == '__main__':
#     # func()
#     # func2()
#     import asyncio
#     asyncio.run(main())


async def func():
    import asyncio
    # import time
    print("我爱你杨幂")
    await asyncio.sleep(2)
    print("我爱你迪丽热巴")
    return 100



if __name__ == '__main__':

    import asyncio
    asyncio.run(func())

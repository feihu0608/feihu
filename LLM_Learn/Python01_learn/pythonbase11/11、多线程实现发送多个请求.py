import requests
import time
import threading
from concurrent.futures import ThreadPoolExecutor
def get_url(url):
    # 最简单的发送http请求 前端往后端发送的请求就是这种请求
    response = requests.get(url)
    print(response.status_code)
    return '哈哈'


if __name__ == '__main__':

    # 单线程 串行  0.9
    # start = time.time()
    # urls = [
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    # ]
    # for url in urls:
    #     get_url(url)
    # end = time.time()
    # print(end - start)



    # 使用多线程
    # start = time.time()
    # urls = [
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    #     "https://www.baidu.com/",
    #     "https://www.jd.com/",
    #     "https://www.taobao.com/",
    #     "https://www.atguigu.com/",
    # ]
    #
    # thread_list = [threading.Thread(target=get_url,name=f"thread{i}",args=(url,)) for i,url in enumerate(urls) ]
    # for t in thread_list:
    #     t.start()
    #
    # # join不要和start放在一起
    # for t in thread_list:
    #     t.join()
    #
    # end = time.time()
    # print(end - start)


    # 试用线程池
    # 线程池是后期我们要用多线程的主要手段，只是python当中几乎不用多线程（因为后期有协程）

    start = time.time()
    urls = [
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
        "https://www.baidu.com/",
        "https://www.jd.com/",
        "https://www.taobao.com/",
        "https://www.atguigu.com/",
    ]
    result_list = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        # executor.submit() 通常用来提交不同的任务
        # executor.map() 通过用来提交相同的任务

        # result = executor.map(get_url, urls)
        # # result是函数返回值的生成器，如果需要返回值要遍历生成器
        # for r in result:
        #     print(r)


        for url in urls:
            result = executor.submit(get_url, url)
            result_list.append(result)
            # print(result.result()) #阻塞 因为他返回的是futrue对象，它里面后期会拿到任务的返回值，但是此时不一定有，只能等
        for r in result_list:
            print(r.result())

    end = time.time()
    print(end - start)





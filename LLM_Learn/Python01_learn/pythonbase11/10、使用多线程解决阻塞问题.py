import time
import threading
def fn1():
    print(threading.current_thread().name) #可以打印子线程的名字
    print("我爱你杨幂")
    time.sleep(2)
    print("我爱你赵丽颖")

def fn2():
    print(threading.current_thread().name)
    print("我爱你迪丽热巴")
    time.sleep(2)
    print("我爱你马尔扎哈")


if __name__ == '__main__':
    print(threading.current_thread().name) #可以打印主线程的名字
    # start = time.time()
    # fn1()
    # fn2()
    # end = time.time()
    # print(end - start)
    # 出现阻塞 串行

    # 使用多线程
    start = time.time()
    t1 = threading.Thread(target=fn1,name="thread01",args=())
    print(threading.current_thread().name)
    t2 = threading.Thread(target=fn2,name="thread02",args=())
    t1.start()
    t2.start()
    t1.join() #让主线程等待子线程执行结束
    t2.join()
    end = time.time()
    print(end - start)




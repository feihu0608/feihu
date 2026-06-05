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


class MyThread(threading.Thread):
    def __init__(self,target,name,args=()):
        super().__init__()  #必须调用父类初始化
        self.target = target
        self.name = name
        self.args = args

    def run(self):
#         指定任务去执行
#         这个是线程类当中启动线程执行任务的方法，调用start就会执行这个run方法
        self.target(*self.args)







if __name__ == '__main__':
    # print(threading.current_thread().name) #可以打印主线程的名字
    # start = time.time()
    # fn1()
    # fn2()
    # end = time.time()
    # print(end - start)
    # 出现阻塞 串行

    # 使用多线程1
    # start = time.time()
    # t1 = threading.Thread(target=fn1,name="thread01",args=())
    # print(threading.current_thread().name)
    # t2 = threading.Thread(target=fn2,name="thread02",args=())
    # t1.start()
    # t2.start()
    # t1.join() #让主线程等待子线程执行结束
    # t2.join()
    # end = time.time()
    # print(end - start)

    # 使用多线程2
    start = time.time()
    t1 = MyThread(target=fn1,name="thread1",args=())
    print(threading.current_thread().name)
    t2 = MyThread(target=fn2,name="thread2",args=())
    t1.start()
    t2.start()
    t1.join() #让主线程等待子线程执行结束
    t2.join()
    end = time.time()
    print(end - start)


# 类实现多线程写起来麻烦，但是可以定制start的逻辑，逻辑写在run当中
# 后期如果不定制，几乎用的全是第一种方式
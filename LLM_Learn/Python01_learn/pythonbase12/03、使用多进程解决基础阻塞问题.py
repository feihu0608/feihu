import time
import multiprocessing
def fn1():
    print(multiprocessing.current_process().name)
    print("我爱你杨幂")
    time.sleep(2)
    print("我爱你赵丽颖")

def fn2():
    print(multiprocessing.current_process().name)
    print("我爱你迪丽热巴")
    time.sleep(2)
    print("我爱你马尔扎哈")


class MyProcess(multiprocessing.Process):
    def __init__(self,target,name,args=()):
        super().__init__()
        self.target = target
        self.name = name
        self.args = args

    def run(self):
        self.target(*self.args)

if __name__ == '__main__':
    # 串行
    # start = time.time()
    # fn1()
    # fn2()
    # end = time.time()
    # print(end - start)

    print(multiprocessing.current_process().name)
    # 多进程执行
    start = time.time()
    # p1 = multiprocessing.Process(target=fn1,name="pro01",args=())
    # p2 = multiprocessing.Process(target=fn2,name="pro02",args=())

    # 使用进程类
    p1 = MyProcess(target=fn1, name="pro01", args=())
    p2 = MyProcess(target=fn2, name="pro02", args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    end = time.time()
    print(end - start)

# 虽然多进程也可以解决基础阻塞，但是和多线程原理是不一样的  多线程因为共享资源共享GIL，所以是并发
# 多进程是并行，但是资源是之前的n倍
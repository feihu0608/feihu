import time
from concurrent.futures import ThreadPoolExecutor
import threading


count = 0

# 创建锁
lock = threading.Lock()

def count_num(n):
    global count
    for i in range(n):
        lock.acquire() #上锁 其余线程执行到这里全部强制等待
        num = count
        time.sleep(0)
        num += 1
        count = num
        lock.release() #解锁，数据操作完成安全解锁，让其它线程有机会操作
        # count += 1




if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=2) as executor:
        executor.map(count_num, [1000,1000])

    print(count)


# 线程是不安全的，此时我们就得使用线程锁（互斥锁）来解决这个问题
# 以后只要碰到是多线程在操作全局变量，无脑加锁




from concurrent.futures import ProcessPoolExecutor
import multiprocessing
def producer(q):
    q.put("我爱你杨幂")
    q.put("我爱你蜜雪冰城")
    q.put([1,2,3,4])
    q.put(None)

def consumer(q):
    # 消费数据
    while True:
        data = q.get()
        if data is None:
            break
        print(data)


if __name__ == '__main__':

    # 本质就是创建一个队列，把这个队列给每个子进程传递参数
    # q= multiprocessing.Queue()  #这个q专门是给多进程使
    # p1 = multiprocessing.Process(target=producer, args=(q,))
    # p2 = multiprocessing.Process(target=consumer, args=(q,))
    # p1.start()
    # p2.start()
    # p1.join()
    # p2.join()


    # 如果我们使用进程池，那么上面的q不能使用
    manager = multiprocessing.Manager()
    q = manager.Queue()
    with ProcessPoolExecutor(max_workers=2) as executor:
        executor.submit(producer,q)
        executor.submit(consumer,q)





import time
import multiprocessing
from concurrent.futures import ProcessPoolExecutor
def get_sum(n):
    sum1 = 0
    for i in range(1,n+1):
        sum1 += i
    print(sum1)



if __name__ == '__main__':  #假设这个文件倍当做模块去使用，这里的代码不走

    # 串行
    # start = time.time()
    # get_sum(100000000)
    # get_sum(100000000)
    # end = time.time()
    # print(end - start)


#     多进程实现
#     start = time.time()
#     p1 = multiprocessing.Process(target=get_sum, args=(100000000, ))
#     p2 = multiprocessing.Process(target=get_sum, args=(100000000, ))
#     p1.start()
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time.time()
#     print(end - start)

#     多进程在实现计算量比较大的时候有优势，计算量比较小的时候还不如串行
#  多进程实现如果计算量小，决定最终时间长短是由资源的分配和切换以及销毁
#  此时创建、分配、销毁占用的时间比计算时间要长的多，计算时间可以忽略

#  随着计算量增大，决定最终时间长短是由计算时间决定的
#  创建进程、销毁、切换时间可以忽略了



# 进程池实现
    start = time.time()
    with ProcessPoolExecutor(max_workers=2) as executor:
        # result_generator = executor.map(get_sum, [100000000,100000000])
        executor.submit(get_sum, 100000000)
        executor.submit(get_sum, 100000000)
    end = time.time()
    print(end - start)













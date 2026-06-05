"""
    队列实现
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    def is_empty(self):
        # 判断队列是否为空
        return self.__size == 0

    def enqueue(self, data):
        node = Node(data)
        # 如果队列的头部为None 说明队列为空
        if self.__head is None:
            # 新增的 元素即作为队首
            self.__head = node
            # 新增的 元素即作为队尾
            self.__tail = node
        else:
            # 原来的队尾的下一个 指向新增的元素
            self.__tail.next = node
            # 新增的元素 作为新的队尾
            self.__tail = node
        self.__size += 1

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        # 取出头部元素数据
        data = self.__head.data
        # 将原来队首的下一个元素作为新的队首
        self.__head = self.__head.next
        # 长度- 1
        self.__size -= 1
        # 如果元素个数为0  则表示队列已空
        if self.__size == 0:
            # 将队尾也指向None
            self.__tail = None
        return data # 返回取出的数据


    def front(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        # 只是返回了数据  并未从队列中取出 属于查看操作
        return self.__head.data


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)

    # 都查看第一个元素  队首
    print(queue.front())
    # 都查看第一个元素  队首
    print(queue.front())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())






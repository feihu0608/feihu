"""
    实现栈数据结构
"""


class Stack:
    def __init__(self):
        self.__size = 0 # 初始化元素个数为0
        self.__items = [] # 初始化空列表

    @property
    def size(self):
        return self.__size

    def is_empty(self):
        # 判断是否为空
        return self.__size == 0

    def push(self, item):
        # 添加元素 直接追加到末尾
        self.__items.append(item)
        self.__size += 1 # 元素个数+ 1

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        # 获取要弹出的元素 弹出默认从栈顶开始 所以是最后一个元素
        item = self.__items[self.__size - 1]

        del self.__items[self.__size - 1] # 弹出元素 即中栈中消失 所以直接删除
        self.__size -= 1 # 元素个数-1
        return item # 返回删除元素

    def peek(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.__items[self.__size - 1]  # 返回查看元素


    def __str__(self):
        pass # 实现遍历

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)

    print(stack.peek())
    print(stack.pop())
    print(stack.peek())



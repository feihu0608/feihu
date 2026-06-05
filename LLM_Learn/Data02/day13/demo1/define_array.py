"""
    手写实现数组
    将检查下标的操作 抽取为函数实现 提高代码的重用性
"""


class Array:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.size = 0 # 表示有效元素的个数 即实际有几个元素
        self.data = [None]  * capacity


    def grow(self):
        # 扩容两倍
        new_capacity = self.capacity * 2
        # 继续将新的数组 填充默认元素
        new_data = [None] * new_capacity

        # 遍历原数组
        for i in range(self.size):
            # 将原数组中的元素 依次  移动到 新的数组 对应的 位置
            new_data[i] = self.data[i]

        # 改变指针  将data 指向新的数组
        self.data = new_data
        # 改变新的容量
        self.capacity = new_capacity


    def is_empty(self):
        """
        判断是否为空
        :return:
        """
        return self.size == 0


    def is_full(self):
        # 判断是否已满
        return self.size == self.capacity


    def add_last(self,element):
        # 先判断是否已满
        if self.is_full():
            # 是 扩容
            self.grow()

        # 添加在末尾的位置
        self.data[self.size]  = element
        self.size += 1



    def insert(self,index,element):
        # 判断下标是否合法
        if index < 0 or index > self.size:
            raise IndexError("index out of range")
        if self.is_full():
            self.grow()
        # 移动元素
        for i in range(self.size,index,-1):
            # 将前边的元素后移一位
            self.data[i] = self.data[i-1]
        # 在对应的位置插入元素
        self.data[index] = element
        self.size += 1 # 数量 + 1



    def remove(self,index):
        # 判断下标合法性
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        # 删除位置开始 后边的元素往前移动一位
        for i in range(index,self.size - 1):
            self.data[i] = self.data[i + 1]

        # 将最后一位设置为None
        self.data[self.size - 1] = None
        # 数量- 1
        self.size -= 1

        # 通常在实际的开发中 会将删除的元素返回给调用者




    def update(self,index,element):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        # 直接修改内容即可
        self.data[index] = element

    def get(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        # 直接返回对应元素
        return self.data[index]

    def __str__(self):
        return str(self.data[:self.size])


    def clear(self):
        for i in range(self.size):
            self.data[i] = None
        self.size = 0

if __name__ == "__main__":
    arr1 = Array()
    arr1.add_last(5)
    arr1.add_last(6)
    arr1.add_last(7)
    print(arr1)

    arr1.insert(0,9)
    print(arr1)
    arr1.insert(1,10)
    print(arr1)


    arr1.remove(1)
    print(arr1)

    print(arr1.get(0))

    arr1.update(0,888)
    print(arr1)



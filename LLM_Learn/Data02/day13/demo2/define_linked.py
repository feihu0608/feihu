
"""
    双向链表实现
    实现
        删除尾部的方法
        根据下标删除指定元素的方法
        遍历的方法 正序遍历 和 逆序遍历
        修改元素
        重写魔法函数__str__
        ctrl + alt + V 生成变量接收返回值
"""


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList:
    def __init__(self):
        # 初始化一个空链表
       self.head = None
       self.tail = None
       self.size = 0


    def get_size(self):
        # 获取长度
        return self.size

    def is_empty(self):
        # 判断是否为空
        return self.size == 0


    def _get_node(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        # 如果小于元素个数中间位数
        if index < self.size // 2:
            # 从前往后找
            current_node = self.head
            for _ in range(index):
                # 依次找到下一个元素
                current_node = current_node.next
            return current_node # 返回元素
        else:
            # 否则表示大于或者等于元素个数中间位数
            current_node = self.tail # 从后往前找
            step = self.size - 1 - index # 计算要查找几步
            for _ in range(step): # 遍历
                # 依次将上一个元素赋值给当前变量
                current_node = current_node.prev
            return current_node # 返回


    def add_first(self,data):
        # 创建对象
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            # 将新添加元素的下一个指向为原来的头 因为我们是添加在头部
            new_node.next = self.head
            # 将原来头部元素的上一个元素 指向当前新增的元素
            self.head.prev = new_node
            # 新添加的元素  作为新的头部
            self.head = new_node
        self.size += 1

    def add_last(self,data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.size += 1


    def insert(self,index,data):
        if index < 0 or index > self.size:
            raise IndexError("index out of range")

        if index == 0:
            self.add_first(data)
        elif index == self.size:
            self.add_last(data)
        else:
            new_node = Node(data)
            curr = self._get_node(index)
            # 找到当前节点的上一个节点
            prev_node = curr.prev
            # 将当前节点的上一个节点的下一个 指向当前插入的节点
            prev_node.next = new_node
            # 插入节点的上一个节点 等于原来位置节点的上一个
            new_node.prev = prev_node

            # 建立new_node 和 curr的连接
            new_node.next = curr
            curr.prev = new_node
            self.size += 1

    def get(self,index):
        # 继续复用我们之前实现的查找功能
        node = self._get_node(index)
        # 返回节点元素的值
        return node.data


    def remove_first(self):
        if self.is_empty():
            raise Exception("linkedlist is empty")
        # 找到要删除的元素
        del_node = self.head
        # 记录要删除元素的值
        del_data = del_node.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            # 将head元素的上一个地址 设置为None 表示断开连接
            self.head.prev = None
            # 将原来的头部节点和其下一个断开连接
            del_node.next = None
        self.size -= 1
        return del_data


    def remove_last(self):
        if self.is_empty():
            raise Exception("linkedlist is empty")
        del_node = self.tail
        del_data = del_node.data

        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            del_node.prev = None
        self.size -= 1
        return del_data


    def remove(self,index):
        if index < 0 or index >= self.size:
            raise IndexError("index out of range")
        if index == 0:
            return self.remove_first()
        elif index == self.size - 1:
            return self.remove_last()
        else:
            del_node = self._get_node(index)
            del_data = del_node.data
            # 获取删除节点前一个节点
            prev_node = del_node.prev
            # 获取删除节点的下一个节点
            next_node = del_node.next

            # 重新关联删除节点的左右两侧
            prev_node.next = next_node
            next_node.prev = prev_node
            # 将删除节点的左右链接 置为None
            del_node.prev = None
            del_node.next = None
            self.size -= 1
            return del_data


    def update(self,index,data):
        node = self._get_node(index)
        node.data = data


    def clear(self):
        curr = self.head
        while curr is not None:
            # 记录下一个即将操作的元素
            next_node = curr.next
            # 当前元素下一个链接为None
            curr.next = None
            # 当前元素上一个链接为None
            curr.prev = None
            # 重新修改当前元素 实现迭代效果
            curr = next_node
        self.head = None
        self.tail = None
        self.size = 0


    def traverse(self):
        # 准备空列表
        result = []
        # 获取头部元素
        curr = self.head
        # 遍历 因为遍历到最后 下一个元素指向None
        while curr is not None:
            # 每次将data保存在result中即可
            result.append(curr.data)
            curr = curr.next  # 每次更新变量
        return result # 返回列表

    def traverse_reverse(self):
        result = []
        curr = self.tail
        while curr is not None:
            result.append(curr.data)
            curr = curr.prev
        return result

    def __str__(self):
        # 因为是覆盖父类的方法 所有返回值只能为str 所以这里强转一下
        return str(self.traverse())

if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.add_first(1)
    dll.add_last(2)
    dll.add_last(3)
    dll.add_first(5)

    print(dll)

    dll.insert(2,666)
    print(dll)


    dll.remove_first()
    print(dll)

    dll.update(0,999)
    print(dll)






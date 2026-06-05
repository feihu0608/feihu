"""
    实现哈希表

    一个安全的hash算法 必须满足以下要求  独一无二的 数值指纹
    1.不可逆
    2.不能存在不同的内容 得到相同的hash值

"""

class Node:
    def __init__(self, key,value,hash_val):
        self.key = key
        self.value = value
        self.hash_val = hash_val
        self.next = None  # 下一个元素默认指向为空


class HashTable:
    LOAD_FACTOR = 0.75
    DEFAULT_CAPACITY = 1 << 4  # 16

    def __init__(self):
        # 初始化数组中的各个元素
        self.table = [None] * self.DEFAULT_CAPACITY
        self.size = 0 # 有效元素

    @staticmethod
    def _hash(key):
        # 这个操作不是必须的 只是可以将最终的hash值控制在 32为宽度的正数范围以内
        return hash(key) & 2147483647

    def _index(self,hash_val):
        # 使用计算以后的hash值 对数组长度-1 进行与运算
        return hash_val & (len(self.table)-1)


    def put(self,key,value):
        # 根据用户传入的键计算到hash值
        _hash = HashTable._hash(key)
        # 根据hash值获取下标
        _index = self._index(_hash)
        # 获取当前下标数组中对应的元素
        current_node = self.table[_index]

        # 如果为None 表示此位置没有元素
        if current_node is  None:
            # 直接存放
            self.table[_index] = Node(key,value,_hash)
            self.size += 1 # 长度+1
        else: # 否则表示此位置有元素 我们无法确定是有一个 还是n个
            while current_node is not None: # 所以遍历 (单向链表)
                # 如果hash值一致 并且 key值也一致
                if current_node.hash_val == _hash and current_node.key == key:
                    current_node.value = value #直接覆盖
                    return # 结束当前函数
                # 更新当前元素 继续迭代
                current_node = current_node.next
            #代码能执行到这里 说明上方没有hash值 和key值 与我们当前插入元素 完全一致的元素
            new_node = Node(key,value,_hash) # 创建新元素
            # 采用 头插法 插入到头部 这样可以提高效率 插入在尾部是O(n)
            # 将新增的元素下一个 指向 原来链表的头部
            new_node.next = self.table[_index]
            self.table[_index] = new_node # 插入头部
            self.size += 1
        # 超出阈值  扩容
        if self.size > len(self.table) * HashTable.LOAD_FACTOR:
            self.resize()

    def resize(self):
        old_cap = len(self.table) # 获取原来的容量
        new_cap = old_cap * 2  # 扩容2倍  数组扩容  长度由原来的16变为32
        new_table = [None] * new_cap

        for head_node in self.table:
            # 定义变量接收 头部元素
            current_node = head_node
            while current_node is not None:
                # 通过头部节点获取到下一个节点
                next_node =  current_node.next
                # 使用当前元素 与新的数组长度进行与运算符 获取到新的下标  范围在0~31
                new_idx = current_node.hash_val & (new_cap - 1)
                # 将当前元素直接头插法 插入到新计算出来的数组对应的位置
                # 有可能还在当前位置 也有可能指向当前位置+增长容量的位置
                # 1.先指向头部
                current_node.next = new_table[new_idx]
                # 2.成为头部
                new_table[new_idx] = current_node
                # 迭代
                current_node = next_node
            # 将原数组 指向 新的数组 后续再访问的即为扩容之后的数组
        self.table = new_table







    def get(self,key):
        # 根据key获取hash值
        _hash = HashTable._hash(key)
        # 根据hash计算下标
        _index = self._index(_hash)

        # 根据下标获取到数组中的元素   但是这个元素不一定是我们所需要的
        current_node = self.table[_index]

        # 所以我们将当前数组位置的整个链表 遍历
        while current_node is not None:
            # 如果hash值相同 并且 key值相同
            if current_node.hash_val == _hash and current_node.key == key:
                return current_node.value # 返回对应的value
            current_node = current_node.next # 继续迭代 更新当前元素

        # 代表能执行到这里 说明未找到 则返回None
        return None


    def remove(self,key):
        _hash = HashTable._hash(key)
        _index = self._index(_hash)
        current_node = self.table[_index]
        # 因为删除元素 需要将当前被删除元素的上一个元素 指向 被删除元素的下一个
        prev_node = None

        while current_node is not None:
            if current_node.hash_val == _hash and current_node.key == key:
                if prev_node is  None:
                    self.table[_index] = current_node.next
                else:
                    prev_node.next = current_node.next
                self.size -= 1
                return current_node.value # 将删除元素的对应的值返回
            # 上一个节点 要随着遍历不断的变化
            prev_node = current_node
            # 当前元素依次更新迭代
            current_node = current_node.next
        return None # 到这里 说明未找到要删除的元素


    def traverse(self):
        for idx,head in enumerate(self.table):
            # 如果当前头部为None
            if head is None:
                continue # 跳过本次循环 开始新的一次

            # 记录当前头部
            current = head

            while current is not None:
                print(f"({current.key} : {current.value})",end="")
                current = current.next # 更新迭代元素
            # 在for循环中的换行 每列换一行
            print()



if __name__ == '__main__':
    hash_table = HashTable()
    hash_table.put("a",11)
    hash_table.put("a",21)
    hash_table.put("a",13)
    hash_table.put("a",41)
    hash_table.put("b",2)
    hash_table.put("c",3)
    hash_table.put("d",4)

    # Java语言中 固定内容的字符串 hash值是永远不变的 (相同版本JDK的情况下) 使用固定的规则进行计算
    # 使用权重31进行计算  因为31是一个特殊的质数 任何数乘以31 等同于这个数 左移5位 减去这个数本身
    print(3038 + 3069 + 3007)


    hash_table.traverse()

    print(2 * 31)
    print((2  << 5) - 2)















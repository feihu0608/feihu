"""
    定义二叉查找树
"""
from collections import deque


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None # 初始左子结点为None
        self.right = None # 初始右子节点为None

class BinarySearchTree:

    def __init__(self):
        self.root = None  # 初始化根节点为None
        self.size = 0  # 初始化树上的节点为0

    def is_empty(self):
        return self.size == 0    # 或者 返回 self.root == None

    def search_pos(self,item):
        # 获取根节点
        current = self.root
        # 初始化一个父节点 为None
        parent = None

        while current is not None:
            if item == current.data:
                # 找到了节点的位置  直接结束循环
                break
            elif item < current.data:
                # 从左边找
                parent = current
                current = current.left
            else:
                # 从右边找
                parent = current
                current = current.right
        return  current,parent

    def add(self,item):
        # 构造一个Node对象
        new_node = Node(item)

        # 如果树为空
        if self.is_empty():
            # 直接添加到根节点
            self.root = new_node
            # 元素个数+ 1
            self.size += 1
            return  # 添加完毕函数结束
        # 这里找到的节点 一个当前节点 一个父节点
        current , parent = self.search_pos(item)

        # 如果获取到的应该插入位置的当前节点不为None  说明添加了重复的元素
        if current is not None:
            return # 直接结束函数

        # 如果添加的元素小于父节点
        if item < parent.data:
            # 存放在左边
            parent.left = new_node
        else:
            # 存放在右边
            parent.right = new_node
        # 元素个数+ 1
        self.size += 1

    def _get_min(self,node):
        # 接收传入的参数  要根据用户传入的某个节点 来找到此节点下最小的元素
        current = node
        # 最小的永远在最左边 所以 重复遍历最左边即可
        # 直到当前节点的左节点为空 说明 当前节点即为最小节点
        while current.left is not None:
            current = current.left # 更新变量
        return current # 返回最小的节点

    def remove(self,item):
        # 根据传入的数据 找到对应的 位置(节点)
        current,parent = self.search_pos(item)

        # 如果找到的节点为None 表示不存在
        if current is None:
            return  # 则直接结束函数

        # 情况1 删除的为叶子节点 左右都为None
        if current.left is None and current.right is None:
            # 如果父节点为None 表示删除的为根节点
            if parent is None:
                self.root = None # 置空根节点
            # 如果根当前节点的左边相同 就将左节点置空
            elif parent.left == current:
                parent.left = None
            else:
                # 否则将右节点置空
                parent.right = None
        # 情况2 只有一个孩子的情况 (左边为空或者右边为空)
        elif current.left is None or current.right is None:
            # 如果左边节点不为空 则child为左节点 否则为右节点
            child = current.left if current.left else current.right

            # 如果删除节点的父节点为空 说明我们要删除的就是根节点
            if parent is None:
                # 将其原本的子节点作为新的根节点
                self.root = child
            elif parent.left == current:
                # 将删除节点的父节点 指向删除节点的子节点
                parent.left = child
            else:
                parent.right = child
        # 情况3  有两个孩子
        else:
            # 根据右边节点 找到了最小的节点
            min_node = self._get_min(current.right)
            # 将最小节点的值保存
            min_data = min_node.data
            # 删除当前节点
            self.remove(min_data)
            # 将已经保存的最小节点的值 存放在删除位置 即可
            current.data = min_data
            return # 表示递归调用以后 不再往下执行-1操作
        self.size -= 1


# ==================== 四种遍历 ====================
    def for_each(self, func, order="inorder"):
        """
        统一遍历接口
        :param func: 对每个节点执行的函数
        :param order: 遍历方式
                preorder   前序
                inorder    中序（默认）
                postorder  后序
                levelorder 层序
        """
        if order == "preorder":
            self.__preorder(self.root, func)
        elif order == "inorder":
            self.__inorder(self.root, func)
        elif order == "postorder":
            self.__postorder(self.root, func)
        elif order == "levelorder":
            self.__levelorder(func)

    def __preorder(self, node, func):
        """
        前序遍历：根 → 左 → 右
        """
        if node is not None:
            func(node.data)               # 根
            self.__preorder(node.left, func)   # 左
            self.__preorder(node.right, func)  # 右

    def __inorder(self, node, func):
        """
        中序遍历：左 → 根 → 右
        特点：二叉搜索树中序结果一定是 升序
        """
        if node is not None:
            self.__inorder(node.left, func)    # 左
            func(node.data)               # 根
            self.__inorder(node.right, func)   # 右

    def __postorder(self, node, func):
        """
        后序遍历：左 → 右 → 根
        """
        if node is not None:
            self.__postorder(node.left, func)  # 左
            self.__postorder(node.right, func) # 右
            func(node.data)               # 根

    def __levelorder(self, func):
        """
        层序遍历：从上到下，从左到右
        用队列实现
        """
        if self.is_empty():
            return

        queue = deque()
        queue.append(self.__root)

        while queue:
            # 出队一个节点
            node = queue.popleft()
            # 访问当前节点
            func(node.data)
            # 左孩子入队
            if node.left:
                queue.append(node.left)
            # 右孩子入队
            if node.right:
                queue.append(node.right)

    # ==================== 课堂展示：打印树结构 ====================
    def print_tree(self):
        """
        按层打印树结构，方便课堂直观展示
        """
        # 内部函数：求树的高度
        def get_height(node):
            if not node:
                return 0
            return max(get_height(node.left), get_height(node.right)) + 1

        height = get_height(self.root)
        queue = deque()
        queue.append((self.root, 1))  # (节点，当前在第几层)
        current_level = 1

        while queue:
            node, level = queue.popleft()

            # 层数变了，就换行
            if level > current_level:
                print()
                current_level = level

            # 计算居中宽度，保证打印对齐
            width = 20 * height // (2 ** (level - 1))
            val = str(node.data) if node else "N"
            print(f"{val:^{width}}", end="")

            # 继续加入下一层节点
            if level < height:
                queue.append((node.left if node else None, level + 1))
                queue.append((node.right if node else None, level + 1))

        print()

if __name__ == "__main__":

    tree = BinarySearchTree()

    nums = [5,3,7,2,4,6,8]


    for item in nums:
        tree.add(item)

    tree.remove(5)

    print(tree.size)

    tree.print_tree()


    tree.for_each(print,order="inorder")







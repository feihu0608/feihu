"""
    堆排序
    1.从下往上构建大顶堆(小顶堆) 从最后一个父节点开始 n // 2 - 1
    2.以i为父节点的左子结点 2 * i + 1
    3.以i为父节点的右子结点 2 * i + 2
    4.第一轮构建顶堆 是从下往上 后续每一轮都是从上往下构建
"""

def heapify(arr, n, i):
    """
    :param arr: 数组
    :param n: 长度
    :param i: 某个父节点
    :return:
    """
    largest = i  # 假设当前节点为最大节点(下标)

    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        # 递归操作 数组不变 长度不变
        # 第三个参数 largest 因为构建大顶堆以后 有下沉的元素 可能导致下边的结构不符合大顶堆了 所以 需要重写构建
        heapify(arr, n, largest)

def heap_sort(arr):
    # 获取数组长度
    n = len(arr)

    # 从下往上构建大顶堆
    for i in range(n // 2 - 1  , -1   , -1  ):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]

        # 重新维护大顶堆
        # 有效长度减少为i 排除后边已经有序的元素
        # 从根节点0开始 从上往下修复大顶堆 无需全局重建
        heapify(arr, i, 0)


if __name__ == '__main__':
    arr = [1, 5, 3, 4, 2]
    heap_sort(arr)
    print(arr)
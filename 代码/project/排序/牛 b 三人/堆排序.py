import random


def sift(data_list, low, high):
    """

    :param data_list: 列表
    :param low: 堆的根节点
    :param high: 堆的最后一个元素的位置
    :return:
    """
    i = low  # 指向根结点
    j = 2 * i + 1  # 左孩子
    tmp = data_list[low]  # 存放堆顶

    while j <= high:  # 只要左有数
        if j + 1 <= high and data_list[j + 1] > data_list[j]:  # 如果右孩子有数并且比较大
            j += 1  # 指向右孩子
        if data_list[j] > tmp:
            data_list[i] = data_list[j]
            i = j  # 往下一层
            j = 2 * i + 1
        else:  # tmp 更大，把tmp放到i的位置上
            data_list[i] = tmp  # 把 tmp 放到某一级领导上
            break
    data_list[i] = tmp  # 把 tmp 放到叶子节点上


def heap_sort(data_list):
    n = len(data_list)
    for i in range((n - 2) // 2, -1, -1):
        # i 表示建堆的时候调整的部分的根的下标
        sift(data_list, i, n - 1)
    # 堆建立完成
    for i in range(n - 1, -1, -1):
        # i 指向当前堆的最后一个元素
        data_list[0], data_list[i] = data_list[i], data_list[0]
        sift(data_list, 0, i - 1)  # i - 1是新的high


data = [random.randint(1, 100) for i in range(10)]
print(data)
heap_sort(data)
print(data)

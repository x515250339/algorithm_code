import random

"""
1. 比较相邻两个数据如果。第一个比第二个大，就交换两个数
2. 对每一个相邻的数做同样1的工作，这样从开始一队到结尾一队在最后的数就是最大的数。
3. 针对所有元素上面的操作，除了最后一个。
4. 重复1~3步骤，直到顺序完成。
"""


def bubble_sort(li):
    """
    冒泡排序 时间复杂度O(n²)
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]


"""
优化
"""


def bubble_sort(li):
    """
    冒泡排序 时间复杂度O(n²)
    :param li:
    :return:
    """
    # 循环 n 遍
    for i in range(len(li) - 1):
        # 检测是否下一次循环有变更 无变更说明有序
        exchange = False
        # 排过去之后就固定了 固定0 1 2 3 4 ... 所以 - i 算法就是为了优化
        for j in range(len(li) - i - 1):
            # 当现在 比 下一位大，则交换位置
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break


li = [random.randint(0, 100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)

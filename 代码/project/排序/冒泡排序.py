import random


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
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                exchange = True
        if not exchange:
            break


li = [random.randint(0, 100) for i in range(10)]
print(li)
bubble_sort(li)
print(li)

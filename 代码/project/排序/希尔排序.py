def insert_sort_gap(li, gap):
    """
    希尔排序  最坏情况 O(n²) 平均情况小于 O(n²)
    :param li:
    :param gap:
    :return:
    """
    for i in range(gap, len(li)):
        tmp = li[i]
        j = i - gap
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


import random

li = [random.randint(1, 1000) for _ in range(100)]
print(li)
shell_sort(li)
print(li)

import random


def insert_sort(li):
    """
    插入排序 时间复杂度 O(n²)
    :param li:
    :return:
    """
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j + 1] = li[j]
            j = j - 1
        li[j + 1] = tmp


li = [random.randint(0, 100) for i in range(10)]
print(li)
insert_sort(li)
print(li)

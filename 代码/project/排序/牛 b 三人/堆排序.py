def sift(data, low, high):
    root = low
    child = 2 * root + 1
    tmp = data[root]
    while child <= high:
        if child + 1 <= high and data[child] < data[child + 1]:
            child += 1
        if tmp < data[child]:
            data[root] = data[child]
            root = child
            child = 2 * root + 1
        else:
            break
    data[root] = tmp


def heap_sort(data):
    """
     空间复杂度O(1)
    :param data:
    :return:
    """
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)


import random

data = [random.randint(1, 100) for i in range(10)]
print(data)
heap_sort(data)
print(data)

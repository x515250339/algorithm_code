def merge(data, low, mid, high):
    i = low
    j = mid + 1
    tmp = []

    while i <= mid and j <= high:
        if data[i] < data[j]:
            tmp.append(data[i])
            i += 1
        else:
            tmp.append(data[j])
            j += 1

    while i <= mid:
        tmp.append(data[i])
        i += 1
    while j <= high:
        tmp.append(data[j])
        j += 1

    data[low: high + 1] = tmp


def merge_sort(data, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(data, low, mid)
        merge_sort(data, mid + 1, high)
        merge(data, low, mid, high)


import random

data = [i for i in range(10)]
random.shuffle(data)
print(data)
merge_sort(data, 0, len(data) - 1)
print(data)

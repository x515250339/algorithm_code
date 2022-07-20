import random


def select_sort(li):
    """
    插入排序 时间复杂度 O(n²)
    :param li:
    :return:
    """
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j

        li[i], li[min_loc] = li[min_loc], li[i]


li = [random.randint(0, 100) for i in range(10)]
print(li)
select_sort(li)
print(li)

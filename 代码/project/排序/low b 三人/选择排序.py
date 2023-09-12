import random

"""
1. 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
2. 从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾
3. 以此类推，直到所有元素均排序完毕。 
"""


def select_sort(li):
    """
    插入排序 时间复杂度 O(n²)  空间复杂度O(1)
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

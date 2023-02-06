import random
from typing import List


def binary_search(li: [int], val: int) -> int:
    """
    二分查找 时间复杂度 O(log n)

    :param li: 输入列表
    :param val: 返回查询到的索引
    :return:
    """
    left = 0
    right = len(li) - 1
    while left <= right:
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        else:
            left = mid + 1
    return -1


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binary_search(li, 0))


def binary_search(data: List[int], tar: int) -> bool:
    start, end = 0, len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == tar:
            return True
        if data[mid] < tar:
            start = mid + 1
        else:
            end = mid - 1
    return False


def binary_search_bytedance(data_list: List[int], val: int) -> bool:
    if not data_list:
        return False
    start, end = 0, len(data_list) - 1

    while start + 1 < end:
        mid = (start + end) // 2
        if data_list[mid] == val:
            return True
        if data_list[mid] < val:
            start = mid
        else:
            end = mid

    if data_list[start] == val or data_list[end] == val:
        return True

    return False


li = [random.randint(1, 100) for _ in range(50)]
li.sort()
print(li)
# print(binary_search(li, 10))
print(binary_search_bytedance(li, 10))

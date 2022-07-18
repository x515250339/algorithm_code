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
print(binary_search(li, 3))

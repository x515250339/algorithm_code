import random


def partition(li, left, right):
    tmp = li[left]
    while left < right:
        # 从右面找比 tmp 小的值
        while left < right and li[right] >= tmp:
            # 往前走一步
            right -= 1
        # 把右边的值写道左边的空位上
        li[left] = li[right]
        while left < right and li[left] <= tmp:
            left += 1
        # 把左边的值写到右边的空位上
        li[right] = li[left]
    # 把 tmp 归位
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    """
    快速排序 时间复杂度O(n log n)  空间复杂度O(1)
    :param li:
    :param left:
    :param right:
    :return:
    """
    # 至少两个元素
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid - 1)
        quick_sort(li, mid + 1, right)


li = list(range(10000))
random.shuffle(li)
quick_sort(li, 0, len(li) - 1)
print(li)

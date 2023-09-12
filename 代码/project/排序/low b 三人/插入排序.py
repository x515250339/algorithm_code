import random

"""
1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
6. 重复步骤2~5。
"""


def insert_sort(li):
    """
    插入排序 时间复杂度 O(n²)  空间复杂度O(1)
    :param li:
    :return:
    """
    # 循环开始
    for i in range(1, len(li)):
        # 获取第二个值
        tmp = li[i]
        # 第一个索引下标
        j = i - 1
        # 当满足循环条件，j 没有超出索引边界，然后开始比较第一个值（前一个值）和下一个值，以此类推
        while j >= 0 and li[j] > tmp:
            # 交换位置
            li[j + 1] = li[j]
            # 索引-1继续比较
            j = j - 1
        print()
        # 交换位置，小的往前
        li[j + 1] = tmp


li = [random.randint(0, 100) for i in range(10)]
print(li)
insert_sort(li)
print(li)

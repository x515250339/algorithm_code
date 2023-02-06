def bucket_sort(li, n=100, max_num=1000):
    """
    桶排序 时间复杂度 O(n+k) 最坏情况 O(n²+k) 空间复杂度 O(nk)
    :param li:
    :param n:
    :param max_num:
    :return:
    """
    buckets = [[] for _ in range(n)]  # 创建桶
    for v in li:
        i = min(v // (max_num // n), n - 1)  # i 表示 v 放到几号桶
        buckets[i].append(v)  # 把 v 加到桶里
        # 保持桶内的顺序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


import random

li = [random.randint(1, 1000) for _ in range(100)]
print(li)
li = bucket_sort(li)
print(li)

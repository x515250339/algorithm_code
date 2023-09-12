def radix_sort(data_list):
    max_num = max(data_list)  # 最大值 9->1,99->2,888->3
    print(max_num)
    it = 0
    while 10 ** it <= max_num:
        buckets = [[] for _ in range(10)]
        for var in data_list:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
        # 分桶完毕
        data_list.clear()
        for buc in buckets:
            # 重新写入
            data_list.extend(buc)

        it += 1


import random

li = list(range(1000))
random.shuffle(li)
radix_sort(li)
print(li)

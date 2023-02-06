def count_sort(data_list, max_count=100):
    count = [0 for _ in range(max_count + 1)]
    for val in data_list:
        count[val] += 1
    data_list.clear()
    for i, v in enumerate(count):
        for j in range(v):
            data_list.append(i)


import random

li = [random.randint(1, 100) for i in range(100)]
random.shuffle(li)
print(li)
count_sort(li)
print(li)

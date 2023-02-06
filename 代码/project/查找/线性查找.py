def linear_search(data_list, val):
    """
    线性查找 时间复杂度 O(n)

    :param data_list: 输入列表
    :param val: 返回查询到的索引
    :return:
    """
    for i, j in enumerate(data_list):
        if val == j:
            return i


li = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(linear_search(li, 2))

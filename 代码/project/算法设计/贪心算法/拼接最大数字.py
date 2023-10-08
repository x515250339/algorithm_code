"""
有n个非负整数,将其按照字符串拼接的方式拼接为一个整数收。 如何拼接可以使得得到的整数最大?
例:32,94,128,1286,6,71可以拼接除的最大整数为 94716321286128
"""
from functools import cmp_to_key

li = [32, 94, 128, 1286, 6, 71]


def cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    return 0


def number_join(li):
    """
    时间复杂度：O(n)
    空间复杂度：O(n)

    :param li:
    :return:
    """
    li = list(map(str, li))
    li.sort(key=cmp_to_key(cmp))
    return "".join(li)


if __name__ == "__main__":
    print(number_join(li))

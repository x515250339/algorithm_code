# 假设商店老板需要找零n元钱,钱币的面额有:100元、50元、 20元、5元、1元,如何找零使得所需钱币的数量最少?

def change_money(f, n):
    """
    时间复杂度：O(n)
    空间复杂度：O(n)

    :param f:
    :param n:
    :return:
    """
    print(f)
    m = [0 for _ in range(len(f))]
    for i, money in enumerate(f):
        m[i] = n // money
        n = n % money
    return m, n


if __name__ == '__main__':
    f = [100, 50, 10, 5, 1]
    print(change_money(f, 376))

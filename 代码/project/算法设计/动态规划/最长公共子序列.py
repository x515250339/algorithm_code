"""
—个序列的子序列是在该序列中删去若干元素后得 到的序列。
例：“ABCD”和“BDF”都是“ABCDEFG”的子序列
最长公共子序列（LCS）问题：给定两个序列X和Y，求X和Y长度最大的公共子
序列。
例：X="ABCBDAB" Y="BDCABA" LCS(X,Y)="BCBA"
应用场景：字符串相似度比对
"""


def lcs_length(x, y):
    """
    时间复杂度：O(n²)
    空间复杂度：O(n)

    :param x:
    :param y:
    :return:
    """
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


import copy


def lcs(x, y):
    """
    时间复杂度：O(n²)
    空间复杂度：O(n)

    :param x:
    :param y:
    :return:
    """
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = copy.deepcopy(c)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1
            elif c[i - 1][j] > c[i][j - 1]:
                c[i][j] = c[i - 1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3
    return c[m][n], b


def lsc_print(x, y):
    """
    时间复杂度：O(n²)
    空间复杂度：O(n)

    :param x:
    :param y:
    :return:
    """
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:
            res.append(x[i - 1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(res))


print(lsc_print("ABCBDAB", "BDCABA"))

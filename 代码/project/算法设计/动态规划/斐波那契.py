# 递归形式
def febonaqi_recursion(n):
    """
    时间复杂度：O(n²)
    空间复杂度：O(1)

    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return 1
    return febonaqi_recursion(n - 1) + febonaqi_recursion(n - 2)


def febnaqi(n):
    """
    时间复杂度：O(n)
    空间复杂度：O(n)

    :param n:
    :return:
    """
    l = [0, 1, 1]
    if n > 2:
        for i in range(n):
            s = l[-1] + l[-2]
            l.append(s)
    return l[n - 1] + l[n - 2]


print(febonaqi_recursion(33))
print(febnaqi(33))

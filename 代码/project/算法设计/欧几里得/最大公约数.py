def gcd(a, b):
    """
    时间复杂度：O(n)
    空间复杂度：O(1)

    :param a:
    :param b:
    :return:
    """
    if b == 0:
        return a
    return gcd(b, a % b)


def gcd2(a, b):
    """
    时间复杂度：O(n)
    空间复杂度：O(1)

    :param a:
    :param b:
    :return:
    """
    while b > 0:
        r = a % b
        a = b
        b = r
    return a


print(gcd(12, 16))
print(gcd2(12, 16))

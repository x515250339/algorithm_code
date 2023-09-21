# p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]
p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

"""
2n次方

"""


def f1_recursion(p, n):
    if n == 0:
        return 0
    res = p[n]
    for i in range(1, n):
        res = max(res, f1_recursion(p, i) + f1_recursion(p, n - i))
    return res


def f2_recursion(p, n):
    if n == 0:
        return 0
    res = 0
    for i in range(1, n + 1):
        res = max(res, p[i] + f2_recursion(p, n - i))
    return res


"""
n²
重构解
"""


def cut_rod_dp(p, n):
    r = [0]
    for i in range(1, n + 1):
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):
        res_r = 0
        res_s = 0
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)

    return r[n], s


def cut_rod_solution(p, n):
    r, s = cut_rod_extend(p, n)
    ans = []
    while n > 0:
        ans.append(s[n])
        n -= s[n]
    return ans


print(cut_rod_solution(p, 7))

print(cut_rod_dp(p, 10))

# print(f1_recursion(p, 20))
print(f2_recursion(p, 10))

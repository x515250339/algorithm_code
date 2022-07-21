class Solution:
    def addTwoNumbers(self, l1, l2):
        d1 = 0
        for i, v in enumerate(l1):
            if i != 0:
                d1 += v * (10 ** i)
            else:
                d1 += v

        d2 = 0
        for i, v in enumerate(l2):
            if i != 0:
                d2 += v * (10 ** i)
            else:
                d2 += v

        d3 = d2 + d1
        dd = []
        for v in str(d3)[::-1]:
            dd.append(int(v))
        return dd


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
print(Solution().addTwoNumbers(l1, l2))

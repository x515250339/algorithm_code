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


class Solution:
    def addTwoNumbers(self, l1, l2):
        d1 = 0
        d2 = 0
        s = 0
        while l2.next() is None and l1.next() is None:
            s += 1
            if l1.next() is not None:
                val = l1.next()
                if s != 1:
                    d1 += val + (10 ** s)
                else:
                    d1 += val
            if l2.next() is not None:
                val = l1.next()
                if s != 1:
                    d2 += val + (10 ** s)
                else:
                    d2 += val
        s = d1 + d2
        for v in str(s)[::-1]:
            dd.append(int(v))
        return dd


l1 = [9, 9, 9, 9, 9, 9, 9]
l2 = [9, 9, 9, 9]
print(Solution().addTwoNumbers(l1, l2))

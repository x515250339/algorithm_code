"""
462 •目标出现总和
简单•通过率 34%

描述
给一个升序的数组，以及一个target，找到它在数组中出现的次数。
示例
样例1：
输入：[1,3,3,4,5]和target=3,
输出：2.
样例2
输入：[2,2,3,4,6]和target=
4,
输出：1。
样例3：
输入：[1,2,3,4,5]和target= 5,
输出：0。
挑战
时间复杂度在 O(logn) 内
"""


class Solution(object):
    def searchSum(self, i, target):
        start, end = 0, len(i) - 1
        su = 0
        while start + 1 < end:
            mid = (start + end) // 2
            if i[mid] == target:
                su += 1
                start = mid
            elif i[mid] > target:
                end = mid
            else:
                start = mid

        if i[start] == target:
            su += 1
        if i[end] == target:
            su += 1
        return su * target


i = [1, 3, 3, 4, 5]
i = [2, 2, 2]
target = 2
print(Solution().searchSum(i, target))

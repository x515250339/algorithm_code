import copy
from typing import List


class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        nums2 = set()
        for v in nums:
            if v not in nums2:
                nums2.add(v)
            else:
                return v


n = [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 测试结果:0 期望结果:11
print(Solution().findRepeatNumber(n))

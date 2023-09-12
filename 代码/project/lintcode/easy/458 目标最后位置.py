"""
458 •目标最后位置
简单•通过率 42%

描述
—个升序数组，找到 target 最后一次出现的位置，如果没出现过返回

示例
样例1：
输入：nums = [1,2,2,4,5,5], target =2
输出：2

样例2：
输入：nums
= [1,2,2,4,5,5], target = 6
输出：5

标签
二分法
"""


class Solution(object):
    def find_last(self, nums, target):
        """

        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) == 0:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            return end
        elif nums[start] == target:
            return start
        return -1


print(Solution().find_last([8, 8, 8, 8, 8, 8, 8, 8], 1))
print(Solution().find_last([1, 2, 2, 4, 5, 5], 5))
print(Solution().find_last([8, 8, 8, 8, 8, 8, 8, 8], 8))

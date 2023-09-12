"""
39 · 恢复旋转排序数组
算法
简单
通过率
34%
题目
题解
笔记
讨论
排名
描述
给定一个旋转排序数组，在原地恢复其排序。（升序）

什么是旋转数组？

比如，原始数组为[1,2,3,4], 则其旋转数组可以是[1,2,3,4], [2,3,4,1], [3,4,1,2], [4,1,2,3]
样例
样例 1：

输入：

数组 = [4,5,1,2,3]
输出：

[1,2,3,4,5]
解释：

恢复旋转排序数组。

样例 2：

输入：

数组 = [6,8,9,1,2]
输出：

[1,2,6,8,9]
解释：

恢复旋转排序数组。

挑战
使用O(1)的额外空间和O(n)时间复杂度
"""
from typing import List


class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """

    def recover_rotated_sorted_array(self, nums: List[int]):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2

            if nums[mid] > nums[mid + 1]:
                b = mid
            if nums[mid] > nums[mid - 1]:
                start = mid
            else:
                end = mid

        if nums[b] < nums[start]:
            b = start
        if nums[b] < nums[end]:
            b = end
        return nums[b + 1:] + nums[:b + 1]


print(Solution().recover_rotated_sorted_array([4, 5, 1, 2, 3]))

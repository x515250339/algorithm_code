# 给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。
#
#  如果数组中不存在目标值 target，返回 [-1, -1]。
#
#  你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
#  示例 1：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 8
# 输出：[3,4]
#
#  示例 2：
#
#
# 输入：nums = [5,7,7,8,8,10], target = 6
# 输出：[-1,-1]
#
#  示例 3：
#
#
# 输入：nums = [], target = 0
# 输出：[-1,-1]
#
#
#
#  提示：
#
#
#  0 <= nums.length <= 10⁵
#  -10⁹ <= nums[i] <= 10⁹
#  nums 是一个非递减数组
#  -10⁹ <= target <= 10⁹
#
#  Related Topics 数组 二分查找 👍 1824 👎 0
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            left = start
        elif nums[end] == target:
            left = end
        else:
            left = -1

        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[end] == target:
            right = end
        elif nums[start] == target:
            right = start
        else:
            right = -1
        return [left, right]


print(Solution().searchRange([8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8], 8))
print(Solution().searchRange([5, 7, 7, 8, 8, 10], 8))

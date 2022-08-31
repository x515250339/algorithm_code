# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
#
#  请必须使用时间复杂度为 O(log n) 的算法。
#
#
#
#  示例 1:
#
#
# 输入: nums = [1,3,5,6], target = 5
# 输出: 2
#
#
#  示例 2:
#
#
# 输入: nums = [1,3,5,6], target = 2
# 输出: 1
#
#
#  示例 3:
#
#
# 输入: nums = [1,3,5,6], target = 7
# 输出: 4
#
#
#
#
#  提示:
#
#
#  1 <= nums.length <= 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#  nums 为 无重复元素 的 升序 排列数组
#  -10⁴ <= target <= 10⁴
#
#
#  Related Topics 数组 二分查找 👍 1690 👎 0


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2

            if target == nums[mid]:
                return mid

            if target > nums[mid]:
                start = mid
            else:
                end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        if nums[start] > target:
            return 0
        if nums[end] < target:
            return end + 1
        return start + 1


print(Solution().searchInsert([1, 3, 5, 6], 2))
print(Solution().searchInsert([1, 3, 5, 6], 0))
print(Solution().searchInsert([1, 3, 5, 6], 7))
print(Solution().searchInsert([1, 3, 5, 6], 3))
print(Solution().searchInsert([1], 0))

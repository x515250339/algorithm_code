# 整数数组 nums 按升序排列，数组中的值 互不相同 。
#
#  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
# k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
# ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。
#
#  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。
#
#  你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
#
#
#
#  示例 1：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 0
# 输出：4
#
#
#  示例 2：
#
#
# 输入：nums = [4,5,6,7,0,1,2], target = 3
# 输出：-1
#
#  示例 3：
#
#
# 输入：nums = [1], target = 0
# 输出：-1
#
#
#
#
#  提示：
#
#
#  1 <= nums.length <= 5000
#  -10⁴ <= nums[i] <= 10⁴
#  nums 中的每个值都 独一无二
#  题目数据保证 nums 在预先未知的某个下标上进行了旋转
#  -10⁴ <= target <= 10⁴
#
#
#  Related Topics 数组 二分查找 👍 2227 👎 0


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[mid] < target <= nums[-1]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            if nums[0] <= nums[mid]:
                if nums[0] <= target <= nums[mid]:
                    end = mid
                else:
                    start = mid
            else:
                if nums[0] > target >= nums[mid]:
                    start = mid
                else:
                    end = mid

        if nums[start] == target:
            return start
        if nums[end] == target:
            return end
        return -1
# if len(a) == 0:
#     return -1
#
# start, end = 0, len(a) - 1
#
# while start + 1 < end:
#     mid = (start + end) // 2
#     if a[mid] == target:
#         return mid
#     if a[start] <= a[mid]:
#         if a[start] <= target < a[mid]:
#             end = mid
#         else:
#             start = mid
#     else:
#         if a[start] > target > a[mid]:
#             start = mid
#         else:
#             end = mid
#
# if a[start] == target:
#     return start
# if a[end] == target:
#     return end
# return -1

nums = [4, 5, 6, 7, 0, 1, 2]
# nums = [4, 5, 6, 7, 8, 1, 2, 3]
# nums = [3, 5, 1]
# nums = [1, 3, 5]
nums = [5, 1, 3]
target = 3

print(Solution().search(nums, target))

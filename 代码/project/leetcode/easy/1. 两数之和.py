# 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个 整数，并返回它们的数组下标。
#
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
#
#  你可以按任意顺序返回答案。
#
#
#
#  示例 1：
#
#
# 输入：nums = [2,7,11,15], target = 9
# 输出：[0,1]
# 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
#
#
#  示例 2：
#
#
# 输入：nums = [3,2,4], target = 6
# 输出：[1,2]
#
#
#  示例 3：
#
#
# 输入：nums = [3,3], target = 6
# 输出：[0,1]
#
#
#
#
#  提示：
#
#
#  2 <= nums.length <= 10⁴
#  -10⁹ <= nums[i] <= 10⁹
#  -10⁹ <= target <= 10⁹
#  只会存在一个有效答案
#
#
#  进阶：你可以想出一个时间复杂度小于 O(n²) 的算法吗？
#
#  Related Topics 数组 哈希表 👍 14926 👎 0


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, val in enumerate(nums):
            if target - val in dic:
                return [dic[target - val], i]
            dic[nums[i]] = i
        return


class Solution(object):
    def twoSum(self, nums, target):
        """
        时间复杂度 O(n) 空间复杂度O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        for i, val in enumerate(nums):
            if target - val in d:
                return [d[target - val], i]
            d[val] = i
        return


class Solution(object):
    def binary_search(self, li, start, end, target):
        while start + 1 < end:
            mid = (start + end) // 2
            if li[mid][1] == target:
                return mid
            if li[mid][1] < target:
                start = mid
            else:
                end = mid
        if li[start][1] == target:
            return start
        if li[end][1] == target:
            return end
        return

    def twoSum(self, nums, target):
        """
        时间复杂度 O(n) 空间复杂度O(n)
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return
        new_nums = [[i, j] for i, j in enumerate(nums)]
        print(new_nums)
        new_nums.sort(key=lambda x: x[1])

        for i in range(len(new_nums)):
            tmp = target - new_nums[i][1]
            t = self.binary_search(new_nums, i + 1, len(new_nums) - 1, tmp)
            if t:
                return sorted([new_nums[i][0], new_nums[t][0]])
        return


print(Solution().twoSum(nums=[3, 2, 4], target=6))
print(Solution().twoSum(nums=[3, 3], target=6))
print(Solution().twoSum(nums=[3, 2, 3], target=6))

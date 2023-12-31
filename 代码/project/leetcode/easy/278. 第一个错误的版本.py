# 你是产品经理，目前正在带领一个团队开发新的产品。不幸的是，你的产品的最新版本没有通过质量检测。由于每个版本都是基于之前的版本开发的，所以错误的版本之后的所有
# 版本都是错的。 
# 
#  假设你有 n 个版本 [1, 2, ..., n]，你想找出导致之后所有版本出错的第一个错误的版本。 
# 
#  你可以通过调用 bool isBadVersion(version) 接口来判断版本号 version 是否在单元测试中出错。实现一个函数来查找第一个错误
# 的版本。你应该尽量减少对调用 API 的次数。 
# 
#  示例 1： 
# 
#  
# 输入：n = 5, bad = 4
# 输出：4
# 解释：
# 调用 isBadVersion(3) -> false 
# 调用 isBadVersion(5)-> true 
# 调用 isBadVersion(4)-> true
# 所以，4 是第一个错误的版本。
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1, bad = 1
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= bad <= n <= 2³¹ - 1 
#  
# 
#  Related Topics 二分查找 交互 👍 760 👎 0


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    if version == 1150769282 - 1:
        return False
    return True


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n

        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if not isBadVersion(end - 1):
            return end
        if not isBadVersion(start - 1):
            return start
        return -1


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n

        while start + 1 < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid
        if isBadVersion(start):
            return start
        if isBadVersion(end):
            return end
        return -1


# print(Solution().firstBadVersion(2))
# print(Solution().firstBadVersion(5))
print(Solution().firstBadVersion(1420736637))

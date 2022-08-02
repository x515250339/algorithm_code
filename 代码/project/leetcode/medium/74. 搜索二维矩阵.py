# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
#
#
#  每行中的整数从左到右按升序排列。
#  每行的第一个整数大于前一行的最后一个整数。
#
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# 输出：true
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# 输出：false
#
#
#
#
#  提示：
#
#
#  m == matrix.length
#  n == matrix[i].length
#  1 <= m, n <= 100
#  -10⁴ <= matrix[i][j], target <= 10⁴
#
#
#  Related Topics 数组 二分查找 矩阵 👍 690 👎 0


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for i in matrix:
            start = 0
            end = len(i) - 1
            if target > i[end]:
                continue
            while start + 1 < end:
                mid = (start + end) // 2
                if i[mid] == target:
                    return True
                if i[mid] < target:
                    start = mid
                else:
                    end = mid

            if i[start] == target:
                return True
            elif i[end] == target:
                return True
        return False


matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
target = 30
print(Solution().searchMatrix(matrix, target))

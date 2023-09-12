# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：
#
#
#  每行的元素从左到右升序排列。
#  每列的元素从上到下升序排列。
#
#
#
#
#  示例 1：
#
#
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 5
# 输出：true
#
#
#  示例 2：
#
#
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21
# ,23,26,30]], target = 20
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
#  1 <= n, m <= 300
#  -10⁹ <= matrix[i][j] <= 10⁹
#  每行的所有元素从左到右升序排列
#  每列的所有元素从上到下升序排列
#  -10⁹ <= target <= 10⁹
#
#
#  Related Topics 数组 二分查找 分治 矩阵 👍 1087 👎 0


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


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        x, y = len(matrix), len(matrix[0])
        row, col = x - 1, 0
        while row >= 0 and col <= y - 1:
            if matrix[row][col] == target:
                return True
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
        return False


matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]]
target = 5
print(Solution().searchMatrix(matrix, target))

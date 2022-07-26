from typing import List


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        手写硬撸
        :param matrix:
        :param target:
        :return:
        """
        for i in matrix:
            if target in i:
                return True
        return False


class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        """
        参考后 时间复杂度 O(n) 空间复杂度O(1)
        :param matrix:
        :param target:
        :return:
        """
        x, y = len(matrix) - 1, 0
        while x >= 0 and y < len(matrix[0]):
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
        return False


matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

target = 5
# target = 20
print(Solution().findNumberIn2DArray(matrix, target))

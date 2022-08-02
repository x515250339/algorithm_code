"""
描述
写出一个高效的算法来搜索m×n矩阵中的值，返回这个值出现的次数。这个矩阵具有以下特性：每行中的整数从左到右是排序的。每一列的整数从上到下是排序的。
在每一行或每一列中没有重复的整数。

样例
样例 1：

输入：

矩阵 = [[3,4]]
target = 3
输出：

1
解释：

矩阵中只有1个3。

样例 2：

输入：

矩阵 = [
      [1, 3, 5, 7],
      [2, 4, 7, 8],
      [3, 5, 9, 10]
    ]
target = 3
输出：

2
解释：

矩阵中有2个3。

挑战
要求O(m+n) 时间复杂度和O(1) 额外空间

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        m, n = len(matrix), len(matrix[0])
        su = 0
        x, y = 0, m - 1

        while x < n and y >= 0:
            if matrix[y][x] == target:
                su += 1
                x = 0
                y -= 1
                continue
            elif matrix[y][x] > target:
                x = 0
                y -= 1
                continue
            else:
                x += 1
        return su


matrix = [
    [1, 3, 5, 7],
    [2, 4, 7, 8],
    [3, 5, 9, 10]
]
target = 3
print(Solution().searchMatrix(matrix, target))

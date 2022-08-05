"""
图片在计算机处理中往往是使用二维矩阵来表示的。

给你一个大小为 m x n 的二进制矩阵image 表示一张黑白图片，0代表白色像素，1代表黑色像素。

黑色像素相互连接，也就是说，图片中只会有一片连在一块儿的黑色像素。像素点是水平或竖直方向连接的。

给你两个整数 x 和 y 表示某一个黑色像素的位置，请你找出包含全部黑色像素的最小矩形（与坐标轴对齐），并返回该矩形的面积。

你必须设计并实现一个时间复杂度低于O(mn) 的算法来解决此问题。



示例 1：


输入：image = [["0","0","1","0"],["0","1","1","0"],["0","1","0","0"]], x = 0, y = 2
输出：6
示例 2：

输入：image = [["1"]], x = 0, y = 0
输出：1

提示：

m == image.length
n == image[i].length
1 <= m, n <= 100
image[i][j] 为 '0' 或 '1'
1 <= x < m
1 <= y < n
image[x][y] == '1'
image 中的黑色像素仅形成一个 组件

"""
from typing import List


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        row, col = len(image), len(image[0])

        while x < row and y < col:
            image[x][y]


image = [["0", "0", "1", "0"], ["0", "1", "1", "0"], ["0", "1", "0", "0"]]
x = 0
y = 2
print(Solution().minArea(image, x, y))

from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        强行手撸
        :param grid:
        :param k:
        :return:
        """
        if len(grid) <= 1:
            return grid
        sum_grid = sum(grid, [])
        length = len(sum_grid)
        new_grid = [0 for i in range(length)]
        for i in range(0, length):
            if i + k >= length:
                x = abs(length - (i + k))
                if x > length:
                    x = abs(length - (i + k)) % length
                new_grid[x] = sum_grid[i]
            else:
                new_grid[i + k] = sum_grid[i]
        s = []
        a, b = 0, len(grid[0])
        for j in range(1, len(grid) + 1):
            s.append(new_grid[a:b])
            a += len(grid)
            b += len(grid)
        return s


# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# k = 1

grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 4

grid = [[0]]
k = 100

grid = [[1], [2], [3], [4], [7], [6], [5]]
k = 23
"""
[1,2,3]
[4,5,6]
[7,8,9]

|
|

[9,1,2]
[3,4,5]
[6,7,8]
"""
print(Solution().shiftGrid(grid, k))

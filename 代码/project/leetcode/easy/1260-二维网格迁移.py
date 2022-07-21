from typing import List

"""
官方
"""


def shif_grid(grid, k):
    m, n = len(grid), len(grid[0])
    ans = [[0] * n for _ in range(m)]
    for i, row in enumerate(grid):
        for j, v in enumerate(row):
            ind = (i * n + j + k) % (m * n)
            ans[ind // n][ind % n] = v
    return ans


"""
手撸
"""


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        """
        强行手撸
        :param grid:
        :param k:
        :return:
        """
        if len(grid) <= 1:
            if len(grid[0]) <= 1:
                return grid
        sum_grid = sum(grid, [])
        length = len(sum_grid)
        new_grid = [0 for i in range(length)]
        for i in range(0, length):
            if i + k >= length:
                x = abs(length - (i + k))
                if x >= length:
                    x = abs(length - (i + k)) % length
                new_grid[x] = sum_grid[i]
            else:
                new_grid[i + k] = sum_grid[i]
        s = []
        a, b = 0, len(grid[0])
        for j in range(1, len(grid) + 1):
            s.append(new_grid[a:b])
            a += len(grid[0])
            b += len(grid[0])
        return s


# grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# k = 1

grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
k = 4

# grid = [[0]]
# k = 100

# grid = [[1], [2], [3], [4], [7], [6], [5]]
# k = 88
#
# grid = [[-42], [-974], [-631], [594], [-454], [364], [-457], [-885], [312], [-588], [462], [722], [905], [-621], [-915],
#         [-136], [293], [696], [-436], [958], [169], [-220], [10], [-310], [954], [227], [-817], [-45], [-774], [-639],
#         [69], [302], [-984], [-959], [12], [960], [653], [-618]]
# k = 44

# grid = [
#     [215, -322, -930, -619, 334, 367, -381, -629, 731, 197, -340, 333, -150, 899, 683, 405, 461, -104, -556, 301, 962,
#      286, 418, 236, 657, -27, -287, -410, -931]]
# k = 93

# 测试结果:[[215,-322,-930,-619,334,367,-381,-629,731,197,-340,333,-150,899,683,405,461,-104,-556,301,962,286,418,236,657,-27,-287,-410,-931]]
# 期望结果:[[236,657,-27,-287,-410,-931,215,-322,-930,-619,334,367,-381,-629,731,197,-340,333,-150,899,683,405,461,-104,-556,301,962,286,418]]
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
# print(Solution().shiftGrid(grid, k))
print(shif_grid(grid, k))
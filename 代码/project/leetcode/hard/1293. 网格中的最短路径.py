# 给你一个 m * n 的网格，其中每个单元格不是 0（空）就是 1（障碍物）。每一步，您都可以在空白单元格中上、下、左、右移动。
#
#  如果您 最多 可以消除 k 个障碍物，请找出从左上角 (0, 0) 到右下角 (m-1, n-1) 的最短路径，并返回通过该路径所需的步数。如果找不到这样
# 的路径，则返回 -1 。
#
#
#
#  示例 1：
#
#
#
#
# 输入： grid = [[0,0,0],[1,1,0],[0,0,0],[0,1,1],[0,0,0]], k = 1
# 输出：6
# 解释：
# 不消除任何障碍的最短路径是 10。
# 消除位置 (3,2) 处的障碍后，最短路径是 6 。该路径是 (0,0) -> (0,1) -> (0,2) -> (1,2) -> (2,2) -> (3
# ,2) -> (4,2).
#
#
#  示例 2：
#
#
#
#
# 输入：grid = [[0,1,1],[1,1,1],[1,0,0]], k = 1
# 输出：-1
# 解释：我们至少需要消除两个障碍才能找到这样的路径。
#
#
#
#
#  提示：
#
#
#  grid.length == m
#  grid[0].length == n
#  1 <= m, n <= 40
#  1 <= k <= m*n
#  grid[i][j] 是 0 或 1
#  grid[0][0] == grid[m-1][n-1] == 0
#
#
#  Related Topics 广度优先搜索 数组 矩阵 👍 210 👎 0
import collections
from typing import List


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1:
            return 0

        k = min(k, m + n - 3)
        visited = set([(0, 0, k)])
        q = collections.deque([(0, 0, k)])

        step = 0
        while q:
            step += 1
            cnt = len(q)
            for _ in range(cnt):
                x, y, rest = q.popleft()
                for dx, dy in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
                    if 0 <= dx < m and 0 <= dy < n:
                        if grid[dx][dy] == 0 and (dx, dy, rest) not in visited:
                            if dx == m - 1 and dy == n - 1:
                                return step
                            q.append((dx, dy, rest))
                            visited.add((dx, dy, rest))
                        elif grid[dx][dy] == 1 and rest > 0 and (dx, dy, rest - 1) not in visited:
                            q.append((dx, dy, rest - 1))
                            visited.add((dx, dy, rest - 1))
        return -1


class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])

        if m == 1 and n == 1:
            return 1

        k = min(k, m + n - 3)
        visited = set([0, 0, k])
        q = collections.deque([(0, 0, k)])

        step = 0
        while q:
            step += 1
            cnt = len(q)

            for _ in range(cnt):
                x, y, rest = q.popleft()
                for dx, dy in [x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]:
                    if 0 <= dx < m and 0 <= dy < n:
                        if grid[dx][dy] == 0 and (dx, dy, rest) not in visited:
                            if dx == m - 1 and dy == n - 1:
                                return step
                            q.append((dx, dy, step))
                            visited.add((dx, dy, step))
                        elif grid[dx][dy] == 1 and rest > 0 and (dx, dy, rest - 1) not in visited:
                            q.append((dx, dy, step - 1))
                            visited.add((dx, dy, step - 1))


grid = [[0, 0, 0], [1, 1, 0], [0, 0, 0], [0, 1, 1], [0, 0, 0]]
k = 1
print(Solution().shortestPath(grid, k))

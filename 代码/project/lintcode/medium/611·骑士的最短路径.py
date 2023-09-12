"""
骑士的最短路线 · Knight Shortest Path
宽度优先搜索
DP
NetEase
Breadth-first Search
描述
给定骑士在棋盘上的 初始 位置(一个2进制矩阵 0 表示空 1 表示有障碍物)，找到到达 终点 的最短路线，返回路线的长度。如果骑士不能到达则返回 -1 。

起点跟终点必定为空.
骑士不能碰到障碍物.
路径长度指骑士走的步数.

样例
例1:

输入:
[[0,0,0],
 [0,0,0],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
输出: 2
解释:
[2,0]->[0,1]->[2,2]
例2:

输入:
[[0,1,0],
 [0,0,1],
 [0,0,0]]
source = [2, 0] destination = [2, 2]
输出:-1
说明
如果骑士的位置为 (x,y)，他下一步可以到达以下这些位置:

(x + 1, y + 2)
(x + 1, y - 2)
(x - 1, y + 2)
(x - 1, y - 2)
(x + 2, y + 1)
(x + 2, y - 1)
(x - 2, y + 1)
(x - 2, y - 1)
"""
import collections


class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:

    def shortestPath(self, grid, source, destination):
        m = len(grid)
        n = len(grid[0])

        from queue import Queue
        q = Queue()
        q.put(source)
        step = 0

        value = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        while not q.empty():
            size = q.qsize()
            for s in range(size):
                head = q.get()
                if destination.x == head.x and destination.y == head.y:
                    return step
                for dx, dy in value:
                    x, y = head.x + dx, head.y + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y] != 1:
                        grid[x][y] = 1
                        q.put(Point(x, y))
            step += 1
        return -1


class Solution:

    def shortestPath(self, grid, source, destination):
        row, low = len(grid), len(grid[0])
        """
        (x + 1, y + 2)
        (x + 1, y - 2)
        (x - 1, y + 2)
        (x - 1, y - 2)
        (x + 2, y + 1)
        (x + 2, y - 1)
        (x - 2, y + 1)
        (x - 2, y - 1)
        """
        move_step = [(1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1)]
        queue = collections.deque([source])
        step = 0
        while queue:
            for _ in range(len(queue)):
                head = queue.popleft()
                if head.x == destination.x and head.y == destination.y:
                    return step
                for x, y in move_step:
                    _row = head.x + x
                    _low = head.y + y
                    if 0 <= _row < row and 0 <= _low < row and grid[_row][_low] != 1:
                        grid[_row][_low] = 1
                        queue.append(Point(_row, _low))
            step += 1
        return -1


grid = [[0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]]
source = [2, 0]
destination = [2, 2]
print(Solution().shortestPath(grid, Point(2, 0), Point(2, 2)))
grid = [[0, 1, 0],
        [0, 0, 1],
        [0, 0, 0]]
source = [2, 0]
destination = [2, 2]
print(Solution().shortestPath(grid, Point(2, 0), Point(2, 2)))

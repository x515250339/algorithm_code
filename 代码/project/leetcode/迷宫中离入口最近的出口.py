# 1926 https://leetcode.cn/problems/nearest-exit-from-entrance-in-maze/


# 方法一：广度优先搜索
from collections import deque
from typing import List


class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        # 高宽
        m, n = len(maze), len(maze[0])
        # 给定可移动范围 左右 +-1 上下 +-1
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        # 获取当前位置 写入队列, 0为移动步长
        q = deque([(entrance[0], entrance[1], 0)])
        # 将当前位置也看作墙
        maze[entrance[0]][entrance[1]] = "+"
        # 开始寻找出口
        while q:
            # 获取当前位置以及步长
            cx, cy, d = q.popleft()
            # 开始移动 4为上下左右
            for k in range(4):
                # 左右移动
                nx = cx + dx[k]
                # 上下移动
                ny = cy + dy[k]
                # 当前坐标合法，也就是大于0且未超出边界并且在输入的二维数组找到
                if 0 <= nx < m and 0 <= ny < n and maze[nx][ny] == '.':
                    # 新坐标是否为出口，返回距离
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1:
                        return d + 1
                    # 将走过的地方定义为墙
                    maze[nx][ny] = "+"
                    # 继续移动，寻找出口
                    q.append((nx, ny, d + 1))
        # 不存在出口
        return -1


maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]
print(Solution().nearestExit(maze, entrance))

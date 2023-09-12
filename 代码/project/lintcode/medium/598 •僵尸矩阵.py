"""
598 •僵尸矩阵
中等•通过率 45%
끼맨뿌
描述
给一个二维网格，每一个格子都有一个值，2代表墙，1代表僵尸，0代表人类(数字0,1,2)。僵尸每天可以将上下左右最接近的人类感染成僵尸，
但不能穿墙。将所有人类感染为僵尸需要多久，如果不能感染所有人则返回-1。
示例
例1：
输入：
[[0,1,2,0,0],
[1,0,0,2,1],
[0,1,0,0,0]]
输出：
2
例2：
输入：
[[0,0,0],
 [0,0,0],
[0,0,1]
输出：
4
标签
"""
import collections


class Solution(object):
    def zombie(self, zombie):
        zn = len(zombie)

        if zn == 0:
            return -1

        zcn = len(zombie[0])
        res_list = []
        res = 0
        for n in range(zn):
            for zc in range(zcn):
                if zombie[n][zc] == 1:
                    res_list.append((n, zc))
        queue = collections.deque([res_list])
        res_list = []
        while queue:
            for row, col in queue.popleft():
                for x, y in [row + 1, col], [row - 1, col], [row, col + 1], [row, col - 1]:
                    if 0 <= x < zn and 0 <= y < zcn and zombie[x][y] == 0:
                        res_list.append((x, y))
                        zombie[x][y] = 2
            if res_list:
                queue.append(res_list)
                res_list = []
                res += 1
        return res


class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer

    def zombie(self, grid):
        # Write your code here
        sum_zombie = 0
        sum_wall = 0
        n = len(grid)
        m = len(grid[0])
        qzombie = []
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    qzombie.append([i, j, 0])
                    sum_zombie += 1
                elif grid[i][j] == 2:
                    sum_wall += 1

        step = 0
        while qzombie:
            p = qzombie.pop(0)
            for i in range(4):
                x = p[0] + dx[i]
                y = p[1] + dy[i]
                if x < 0 or x >= n or y < 0 or y >= m:
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 1
                    qzombie.append([x, y, p[2] + 1])
                    sum_zombie += 1
            if not qzombie:
                step = p[2]
        if sum_zombie + sum_wall != n * m:
            return -1
        else:
            return step


zombie = [[0, 1, 2, 0, 0],
          [1, 0, 0, 2, 1],
          [0, 1, 0, 0, 0]]
print(Solution().zombie(zombie))

zombie = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 1]]
print(Solution().zombie(zombie))

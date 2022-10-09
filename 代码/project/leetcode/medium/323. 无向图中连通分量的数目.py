"""
323. 无向图中连通分量的数目
你有一个包含 n 个节点的图。给定一个整数 n 和一个数组 edges ，其中 edges[i] = [ai, bi] 表示图中 ai 和 bi 之间有一条边。

返回 图中已连接分量的数目 。



示例 1:



输入: n = 5, edges = [[0, 1], [1, 2], [3, 4]]
输出: 2
示例 2:



输入: n = 5, edges = [[0,1], [1,2], [2,3], [3,4]]
输出:  1


提示：

1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= ai <= bi < n
ai != bi
edges 中不会出现重复的边
通过次数20,035提交次数30,692
"""
import collections
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = collections.defaultdict(list)
        res_count = 0

        for i, j in edges:
            res[i].append(j)
            res[j].append(i)

        visited = set()
        for i in range(n):
            if i not in visited:
                res_count += 1
                visited.add(i)
                queue = collections.deque([i])
                while queue:
                    cur = queue.popleft()
                    for j in res[cur]:
                        if j not in visited:
                            visited.add(j)
                            queue.append(j)
        return res_count


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        result = collections.defaultdict(list)
        res_count = 0

        for i, j in edges:
            result[i].append(j)
            result[j].append(i)

        visited = set()

        for x in range(n):
            if x not in visited:
                res_count += 1
                visited.add(x)
                self.bfs(x, result, visited)
        return res_count

    def bfs(self, x, res, visited):
        queue = collections.deque([x])

        while queue:
            cur = queue.popleft()
            for y in res[cur]:
                if y not in visited:
                    visited.add(y)
                    queue.append(y)


n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(Solution().countComponents(n, edges))
n = 5
edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
print(Solution().countComponents(n, edges))

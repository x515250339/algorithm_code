"""
261. 以图判树
给定编号从 0 到 n - 1 的 n 个结点。给定一个整数 n 和一个 edges 列表，其中 edges[i] = [ai, bi] 表示图中节点 ai 和 bi 之间存在一条无向边。

如果这些边能够形成一个合法有效的树结构，则返回 true ，否则返回 false 。



示例 1：



输入: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
输出: true
示例 2:



输入: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
输出: false


提示：

1 <= n <= 2000
0 <= edges.length <= 5000
edges[i].length == 2
0 <= ai, bi < n
ai != bi
不存在自循环或重复的边
通过次数15,043提交次数29,568
"""
import collections
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        neighbors = collections.defaultdict(list)
        for u, v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)

        visited = {}
        queue = collections.deque([0])
        visited[0] = True

        while queue:
            cur = queue.popleft()
            visited[cur] = True
            for node in neighbors[cur]:
                if node not in visited:
                    visited[node] = True
                    queue.append(node)

        return len(visited) == n


# print(Solution().validTree(5, [[0, 1], [0, 2], [0, 3], [1, 4]]))
print(Solution().validTree(5, [[0, 1], [1, 2], [2, 3], [1, 3]]))

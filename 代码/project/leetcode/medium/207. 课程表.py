# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
#  在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表
# 示如果要学习课程 ai 则 必须 先学习课程 bi 。
#
#
#  例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
#
#
#  请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
#
#
#
#  示例 1：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0]]
# 输出：true
# 解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
#
#  示例 2：
#
#
# 输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
# 输出：false
# 解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。
#
#
#
#  提示：
#
#
#  1 <= numCourses <= 10⁵
#  0 <= prerequisites.length <= 5000
#  prerequisites[i].length == 2
#  0 <= ai, bi < numCourses
#  prerequisites[i] 中的所有课程对 互不相同
#
#
#  Related Topics 深度优先搜索 广度优先搜索 图 拓扑排序 👍 1439 👎 0
import collections
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        edges = collections.defaultdict(list)
        visited = [0] * numCourses
        result = list()
        valid = True

        for info in prerequisites:
            edges[info[1]].append(info[0])

        def dfs(u: int):
            nonlocal valid
            visited[u] = 1
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    valid = False
                    return
            visited[u] = 2
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                dfs(i)

        return valid


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 空 {"":[]}
        edges = collections.defaultdict(list)
        # 多少门课程
        indeg = [0] * numCourses

        # 建立关系
        for info in prerequisites:
            # 谁跟谁关联
            edges[info[1]].append(info[0])
            # 关联多少次，关联的学完之后才可以学
            indeg[info[0]] += 1
        # 先可以学的入队
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        # 记录学了几门
        visited = 0

        while q:
            # 计数 + 1
            visited += 1
            # 出队
            u = q.popleft()
            for v in edges[u]:
                # 关联 - 1
                indeg[v] -= 1
                # 关联为0，可以学习
                if indeg[v] == 0:
                    q.append(v)

        return visited == numCourses


numCourses = 2
prerequisites = [[1, 0]]
print(Solution().canFinish(numCourses, prerequisites))
numCourses = 2
prerequisites = [[1, 0], [0, 1]]
print(Solution().canFinish(numCourses, prerequisites))

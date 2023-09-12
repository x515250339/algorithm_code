"""
搜索图中节点 · Search Graph Nodes
宽度优先搜索
苹果
Breadth-first Search
描述
给定一张 无向图，一个 节点 以及一个 目标值，返回距离这个节点最近 且 值为目标值的节点，如果不能找到则返回 NULL。
在给出的参数中, 我们用 map 来存节点的值

保证答案唯一

样例
例1:

输入:
{1,2,3,4#2,1,3#3,1,2#4,1,5#5,4}
[3,4,5,50,50]
1
50
输出:
4
解释:
2------3  5
 \     |  |
  \    |  |
   \   |  |
    \  |  |
      1 --4
Give a node 1, target is 50

there a hash named values which is [3,4,10,50,50], represent:
Value of node 1 is 3
Value of node 2 is 4
Value of node 3 is 10
Value of node 4 is 50
Value of node 5 is 50

Return node 4
例2:

输入:
{1,2#2,1}
[0,1]
1
1
输出:
2
"""
import collections


class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def searchNode(self, graph, values, node, target):
        queue = collections.deque()
        if values[node] == target:
            return node

        queue.append(node)
        del values[node]

        while queue:
            head = queue.popleft()
            for n in head.neighbors:
                if n in values:
                    if values[n] == target:
                        return n
                    del values[n]
                    queue.append(n)
        return None

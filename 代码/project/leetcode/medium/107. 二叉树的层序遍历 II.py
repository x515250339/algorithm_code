# 给你二叉树的根节点 root ，返回其节点值 自底向上的层序遍历 。 （即按从叶子节点所在层到根节点所在的层，逐层从左向右遍历）
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[15,7],[9,20],[3]]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 2000] 内
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics 树 广度优先搜索 二叉树 👍 615 👎 0


# Definition for a binary tree node.

import collections

from leetcode.utils.util import makeTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue, res = collections.deque([root]), []

        while queue:
            cur_list = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node:
                    continue
                cur_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(cur_list)
        return res[::-1]


class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []

        def dfs(root, level, res):
            if not root:
                return

            if level == len(res):
                res.append([])
            res[level].append(root.val)
            if root.left:
                dfs(root.left, level + 1, res)
            if root.right:
                dfs(root.right, level + 1, res)

        dfs(root, 0, res)
        return res[::-1]


print(Solution().levelOrderBottom(makeTree([3, 9, 20, "null", "null", 15, 7])))

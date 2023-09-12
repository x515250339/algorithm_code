# 给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[9,20],[15,7]]
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
#  Related Topics 树 广度优先搜索 二叉树 👍 1444 👎 0


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.utils.util import makeTree


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        res = []
        queue = [root]

        while queue:
            tmp_list = []

            for _ in range(len(queue)):
                root = queue.pop(0)
                tmp_list.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp_list)
        return res


import collections


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, res = collections.deque([root]), []

        while queue:
            tmp_list = []
            for _ in range(len(queue)):
                root = queue.popleft()
                if not root:
                    continue
                tmp_list.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res.append(tmp_list)
        return res


print(Solution().levelOrder(makeTree([3, 9, 20, 15, 17])))

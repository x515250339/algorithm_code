# 给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。
#
#
#
#  示例 : 给定二叉树
#
#            1
#          / \
#         2   3
#        / \
#       4   5
#
#
#  返回 3, 它的长度是路径 [4,2,1,3] 或者 [5,2,1,3]。
#
#
#
#  注意：两结点之间的路径长度是以它们之间边的数目表示。
#
#  Related Topics 树 深度优先搜索 二叉树 👍 1142 👎 0


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from leetcode.utils.util import makeTree


class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = 1

        def dfs(root):
            if root:
                l = dfs(root.left)
                r = dfs(root.right)
                self.res = max(self.res, l + r)
                return max(l, r) + 1
            return 0

        dfs(root)
        return self.res


print(Solution().diameterOfBinaryTree(makeTree([1, 2, 3, 4, 5])))

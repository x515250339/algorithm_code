# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。
#
#  叶子节点 是指没有子节点的节点。
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：["1"]
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [1, 100] 内
#  -100 <= Node.val <= 100
#
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 794 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import List


class Solution:
    def binaryTreePaths(self, root) -> List[str]:
        r = []

        def binary(root, s):
            if root:
                s += str(root.val)
                if not root.left and not root.right:
                    r.append(s)
                else:
                    binary(root.left, s)
                    binary(root.right, s)

        binary(root, '')
        return r


root = TreeNode(1, TreeNode(2, TreeNode(5)), TreeNode(3))
print(Solution().binaryTreePaths(root))

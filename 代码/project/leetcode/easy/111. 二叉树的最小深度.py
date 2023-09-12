# 给定一个二叉树，找出其最小深度。
#
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
#  说明：叶子节点是指没有子节点的节点。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#
#
#  示例 2：
#
#
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#
#
#
#
#  提示：
#
#
#  树中节点数的范围在 [0, 10⁵] 内
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 817 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        d = 10 ** 4
        if root.left:
            d = min(self.minDepth(root.left), d)
        if root.right:
            d = min(self.minDepth(root.right), d)
        return d + 1


class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        queue = [root]
        res = 1
        while queue:
            for _ in range(len(queue)):
                root = queue.pop(0)
                if not root.left and not root.right:
                    return res
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            res += 1
        return res


# [3,9,20,null,null,15,7]


root = TreeNode(1, TreeNode(2, TreeNode(3)))
root = TreeNode(3, TreeNode(9, TreeNode(20, TreeNode(15), TreeNode(17))))
print(Solution().minDepth(root))

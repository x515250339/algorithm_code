# 给定一个二叉树，判断它是否是高度平衡的二叉树。
#
#  本题中，一棵高度平衡二叉树定义为：
#
#
#  一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。
#
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [1,2,2,3,3,null,null,4,4]
# 输出：false
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：true
#
#
#
#
#  提示：
#
#
#  树中的节点数在范围 [0, 5000] 内
#  -10⁴ <= Node.val <= 10⁴
#
#
#  Related Topics 树 深度优先搜索 二叉树 👍 1110 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        if not root.left and not root.right:
            return True

        def is_bal(root, res):
            if root:
                if root.left:
                    res = is_bal(root.left, res)
                if root.right:
                    res = is_bal(root.right, res)
                res += 1
            return res

        l = is_bal(root.left, 1)
        r = is_bal(root.right, 1)
        print(l, r)
        return abs(l - r) <= 1


# root = TreeNode(1, TreeNode(2, TreeNode(3)))
# [1,2,2,3,3,null,null,4,4]
root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
# root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
print(Solution().isBalanced(root))

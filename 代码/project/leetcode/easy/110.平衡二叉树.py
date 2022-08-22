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

        def height(root):
            if not root:
                return 0
            return max(height(root.left), height(root.right)) + 1

        return abs(height(root.left) - height(root.right)) <= 1 and self.isBalanced(
            root.left) and self.isBalanced(root.right)


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True

        def height(root):
            if not root:
                return 0

            l_h = height(root.left)
            r_h = height(root.right)

            if l_h == -1 or r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            else:
                return max(l_h, r_h) + 1

        return height(root) > 0


# root = TreeNode(1, TreeNode(2, TreeNode(3)))
# [1,2,2,3,3,null,null,4,4]

# [1,2,2,3,null,null,3,4,null,null,4]
# root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(4)), TreeNode(3)), TreeNode(2))
root = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(2, right=TreeNode(3, right=TreeNode(4))))
print(Solution().isBalanced(root))

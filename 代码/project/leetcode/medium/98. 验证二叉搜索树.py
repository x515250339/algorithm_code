# 给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
#
#  有效 二叉搜索树定义如下：
#
#
#  节点的左子树只包含 小于 当前节点的数。
#  节点的右子树只包含 大于 当前节点的数。
#  所有左子树和右子树自身必须也是二叉搜索树。
#
#
#
#
#  示例 1：
#
#
# 输入：root = [2,1,3]
# 输出：true
#
#
#  示例 2：
#
#
# 输入：root = [5,1,4,null,null,3,6]
# 输出：false
# 解释：根节点的值是 5 ，但是右子节点的值是 4 。
#
#
#
#
#  提示：
#
#
#  树中节点数目范围在[1, 10⁴] 内
#  -2³¹ <= Node.val <= 2³¹ - 1
#
#
#  Related Topics 树 深度优先搜索 二叉搜索树 二叉树 👍 1725 👎 0
from leetcode.utils.util import makeTree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root, lower=float('-inf'), upper=float('inf')):
            if not root:
                return True
            v = root.val
            if v <= lower or v >= upper:
                return False
            if not helper(root.left, lower, v):
                return False
            if not helper(root.right, v, upper):
                return False

            return True

        return helper(root)


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def helper(root, upper=float("inf"), lower=float("-inf")):
            if not root:
                return True

            val = root.val

            if lower >= val or upper <= val:
                return False

            if not helper(root.left, val, lower):
                return False
            if not helper(root.right, upper, val):
                return False
            return True

        return helper(root)


root = makeTree([5, 1, 4, "null", "null", 3, 6])
# root = makeTree([2, 1, 3])
print(Solution().isValidBST(root))

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
        if not root:
            return False
        v = root.val
        if root.left:
            if root.left.val < v:
                return True
            else:
                return False
        if root.right:
            print(root.right.val)
            if root.right.val > v:
                return True
            else:
                return False
        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)
        return l & r


root = makeTree([5, 1, 4, None, None, 3, 6])
print(Solution().isValidBST(root))

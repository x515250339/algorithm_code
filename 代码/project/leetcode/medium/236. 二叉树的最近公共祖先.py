# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
#  百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（
# 一个节点也可以是它自己的祖先）。”
#
#
#
#  示例 1：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# 输出：3
# 解释：节点 5 和节点 1 的最近公共祖先是节点 3 。
#
#
#  示例 2：
#
#
# 输入：root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# 输出：5
# 解释：节点 5 和节点 4 的最近公共祖先是节点 5 。因为根据定义最近公共祖先节点可以为节点本身。
#
#
#  示例 3：
#
#
# 输入：root = [1,2], p = 1, q = 2
# 输出：1
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [2, 10⁵] 内。
#  -10⁹ <= Node.val <= 10⁹
#  所有 Node.val 互不相同 。
#  p != q
#  p 和 q 均存在于给定的二叉树中。
#
#
#  Related Topics 树 深度优先搜索 二叉树 👍 1910 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return root

        if root.val == p.val or root.val == q.val:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not right:
            return left
        return right


# [3,5,1,6,2,0,8,null,null,7,4]
# 5,1
root = TreeNode(1, TreeNode(2), TreeNode(3))
root = TreeNode(3, TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4))),
                TreeNode(1, TreeNode((0), TreeNode(8))))
print(Solution().lowestCommonAncestor(root, TreeNode(5), TreeNode(8)).val)

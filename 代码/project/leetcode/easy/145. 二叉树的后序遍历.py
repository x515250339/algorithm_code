# 给你一棵二叉树的根节点 root ，返回其节点值的 后序遍历 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[3,2,1]
#
#
#  示例 2：
#
#
# 输入：root = []
# 输出：[]
#
#
#  示例 3：
#
#
# 输入：root = [1]
# 输出：[1]
#
#
#
#
#  提示：
#
#
#  树中节点的数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？
#
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 897 👎 0


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        s = []

        def postorder(root):
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            s.append(root.val)

        postorder(root)
        return s


class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res, stack = [], []
        prev = None
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if not root.right or root.right == prev:
                res.append(root.val)
                prev = root
                root = None
            else:
                stack.append(root)
                root = root.right
        return res


root = TreeNode(3, TreeNode(1), TreeNode(2))
print(Solution().postorderTraversal(root))

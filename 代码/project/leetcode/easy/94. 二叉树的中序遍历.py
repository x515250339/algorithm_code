# 给定一个二叉树的根节点 root ，返回 它的 中序 遍历 。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,3,2]
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
#  树中节点数目在范围 [0, 100] 内
#  -100 <= Node.val <= 100
#
#
#
#
#  进阶: 递归算法很简单，你可以通过迭代算法完成吗？
#
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 1520 👎 0


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        r = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            r.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)
        return r


class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        dummy = TreeNode()
        dummy.right = root
        stack = [dummy]
        inorder = []
        while stack:
            node = stack.pop()
            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            if stack:
                inorder.append(stack[-1].val)

        return inorder


# root = TreeNode(1, right=TreeNode(2, TreeNode(3)))
root = TreeNode(3, TreeNode(1), TreeNode(2))
# root = TreeNode(1)

print(Solution().inorderTraversal(root))

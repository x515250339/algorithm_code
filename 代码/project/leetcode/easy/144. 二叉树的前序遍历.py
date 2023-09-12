# 给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,null,2,3]
# 输出：[1,2,3]
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
#  示例 4：
#
#
# 输入：root = [1,2]
# 输出：[1,2]
#
#
#  示例 5：
#
#
# 输入：root = [1,null,2]
# 输出：[1,2]
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
#  进阶：递归算法很简单，你可以通过迭代算法完成吗？
#
#  Related Topics 栈 树 深度优先搜索 二叉树 👍 877 👎 0


# Definition for a binary tree node.
import copy


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        r = []

        def preorder(root):
            r.append(root.val)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        preorder(root)
        return r


class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        cur_root, stack = [], []
        while root or stack:
            if root:
                cur_root.append(root.val)
                stack.append(root)
                root = root.left
            else:
                root = stack.pop()
                root = root.right
        return cur_root


class Solution(object):
    def preorderTraversal(self, root):
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


class Solution(object):
    """
    @param root: The root of binary tree.
    @return: Preorder in list which contains node values.
    """

    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return preorder


# root = TreeNode(1, right=TreeNode(2, TreeNode(3)))
root = TreeNode(3, TreeNode(1), TreeNode(2))
# root = TreeNode(1)
print(Solution().preorderTraversal(root))

from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        时间复杂 O(n) 空间复杂度 O(n)
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder and not inorder:
            return
        root = TreeNode(preorder[0])  # 前序遍历第一个为根节点
        # 利用栈
        stack = [root]
        inorderIndex = 0
        for i in range(1, len(preorder)):
            # 前序遍历 根左右
            preorder_val = preorder[i]
            node = stack[-1]
            # 中序遍历 左根右
            if node.val != inorder[inorderIndex]:
                node.left = TreeNode(preorder_val)
                stack.append(node.left)
            else:
                while stack and stack[-1].val == inorder[inorderIndex]:
                    node = stack.pop()
                    inorderIndex += 1
                node.right = TreeNode(preorder_val)
                stack.append(node.right)
        return root


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        递归实现
        :param preorder:
        :param inorder:
        :return:
        """
        if not preorder:
            return

        root = TreeNode(preorder[0])
        idx = inorder.index(root.val)
        root.left = self.buildTree(preorder[1: idx + 1], inorder[:idx])
        root.right = self.buildTree(preorder[idx + 1:], inorder[idx + 1:])
        return root


preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
print(Solution().buildTree(preorder, inorder).val)

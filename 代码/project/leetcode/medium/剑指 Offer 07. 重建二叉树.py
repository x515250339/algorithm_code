from typing import List


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """

        :param preorder:
        :param inorder:
        :return:
        """
        # 前序遍历 根左右
        # 中序遍历 左根右


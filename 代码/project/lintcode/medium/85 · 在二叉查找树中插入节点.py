"""
85 · 在二叉查找树中插入节点
算法
简单
通过率
48%
题目
题解
笔记
讨论
排名
记录
描述
给定一棵二叉查找树和一个新的树节点，将节点插入到树中。

你需要保证该树仍然是一棵二叉查找树。

背完这套刷题模板，真的不一样！

北大学霸令狐冲15年刷题经验总结的《算法小抄模板Cheat Sheet》助你上岸！

微信添加【jiuzhang0607】备注【小抄】领取


保证不会出现重复的值

样例
样例 1：

输入：

tree = {}
node= 1
输出：

{1}
解释：

在空树中插入一个点，应该插入为根节点。

样例 2：

输入：

tree = {2,1,4,#,#,3}
node = 6
输出：

{2,1,4,#,#,3,6}
解释：

如下:
2                              2
/   \                          /   \
1     4          -->       1       4
/                                /  \
3                                3      6

挑战
能否不使用递归？
"""
from leetcode.utils.util import makeTree


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: node: insert this node into the binary search tree
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        if not root:
            return node
        curr = root
        while root:
            if curr.val > node.val:
                if not curr.left:
                    curr.left = node
                    break
                else:
                    curr = curr.left
            else:
                if not curr.right:
                    curr.right = node
                    break
                else:
                    curr = curr.right
        return root


print(Solution().insertNode(makeTree([2, 1, 4, "null", "null", 3]), TreeNode(6)))

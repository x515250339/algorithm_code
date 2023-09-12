# 给定一个二叉树，找出其最大深度。
#
#  二叉树的深度为根节点到最远叶子节点的最长路径上的节点数。
#
#  说明: 叶子节点是指没有子节点的节点。
#
#  示例：
# 给定二叉树 [3,9,20,null,null,15,7]，
#
#      3
#    / \
#   9  20
#     /  \
#    15   7
#
#  返回它的最大深度 3 。
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 1326 👎 0


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def maxDepth(self, root) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


class Solution:

    def maxDepth(self, root) -> int:
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1


from queue import Queue


class Solution:

    def maxDepth(self, root) -> int:
        if not root:
            return 0

        queue = Queue()
        queue.put(root)
        ans = 0
        while not queue.empty():
            sz = queue.qsize()
            while sz > 0:
                node = queue.get()
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                sz -= 1
            ans += 1
        return ans


class Solution:

    def maxDepth(self, root) -> int:
        if not root:
            return 0

        queue = [root]
        s = 0
        while queue:
            for i in range(len(queue)):
                node = queue.pop(0)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            s += 1
        return s


root = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(Solution().maxDepth(root))

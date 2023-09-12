# 给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。
#
#
#
#  示例 1：
#
#
# 输入：root = [3,9,20,null,null,15,7]
# 输出：[[3],[20,9],[15,7]]
#
#
#  示例 2：
#
#
# 输入：root = [1]
# 输出：[[1]]
#
#
#  示例 3：
#
#
# 输入：root = []
# 输出：[]
#
#
#
#
#  提示：
#
#
#  树中节点数目在范围 [0, 2000] 内
#  -100 <= Node.val <= 100
#
#
#  Related Topics 树 广度优先搜索 二叉树 👍 691 👎 0


# Definition for a binary tree node.
import collections

from leetcode.utils.util import makeTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []

        queue, res = [root], []
        reserved = True
        while queue:
            cur_list = []
            if reserved:
                res.append([node.val for node in queue])
            else:
                res.append([node.val for node in queue[::-1]])
            for node in queue:
                if not node:
                    continue
                if node.left:
                    cur_list.append(node.left)
                if node.right:
                    cur_list.append(node.right)
            queue = cur_list
            reserved = not reserved

        return res


class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        if root is None:
            return []
        ans = []
        q = collections.deque([root])
        # 正反向标志
        reserved = 1
        while len(q) is not 0:
            row = []
            for i in range(len(q)):
                if q[0].left:
                    q.append(q[0].left)
                if q[0].right:
                    q.append(q[0].right)
                row.append(q[0].val)
                q.popleft()
            # 根据标志来确认当前层遍历的方向
            row = row[::reserved]  # 翻转
            ans += [row]
            # 方向反转
            reserved *= -1
        return ans


print(Solution().zigzagLevelOrder(makeTree([3, 9, 20, "null", "null", 15, 7])))

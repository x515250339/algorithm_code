# 序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方
# 式重构得到原数据。
#
#  请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串
# 反序列化为原始的树结构。
#
#  提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅 LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的
# 方法解决这个问题。
#
#
#
#  示例 1：
#
#
# 输入：root = [1,2,3,null,null,4,5]
# 输出：[1,2,3,null,null,4,5]
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
#
#
#  提示：
#
#
#  树中结点数在范围 [0, 10⁴] 内
#  -1000 <= Node.val <= 1000
#
#
#  Related Topics 树 深度优先搜索 广度优先搜索 设计 字符串 二叉树 👍 972 👎 0
from leetcode.utils.util import makeTree


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1

        while queue[-1] is None:
            queue.pop()

        return '{%s}' % ','.join([str(node.val) if node is not None else '#' for node in queue])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')

        if data == '{}':
            return None

        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0

        for val in vals[1:]:
            if val != '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root is None:
            return "{}"

        queue = [root]
        index = 0
        while index < len(queue):
            if queue[index] is not None:
                queue.append(queue[index].left)
                queue.append(queue[index].right)
            index += 1

        while queue[-1] is None:
            queue.pop()

        res = []
        for node in queue:
            if node is not None:
                res.append(str(node.val))
            else:
                res.append("#")
        return '{%s}' % ','.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.strip('\n')

        if data == '{}':
            return None

        vals = data[1:-1].split(',')

        root = TreeNode(int(vals[0]))
        queue = [root]
        isLeftChild = True
        index = 0

        for val in vals[1:]:
            if val != '#':
                node = TreeNode(int(val))
                if isLeftChild:
                    queue[index].left = node
                else:
                    queue[index].right = node
                queue.append(node)

            if not isLeftChild:
                index += 1
            isLeftChild = not isLeftChild

        return root


root = makeTree([1, 2, 3, "null", "null", 4, 5])
root = makeTree([1, 2, 3, 7, "null", 4, 5])
data = Codec().serialize(root)
print(data)
print(Codec().deserialize(data))

class Tree:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# 生成树
T = Tree("D", Tree("B", Tree("A"), Tree("C")), Tree("E", right=Tree("G", Tree("F"))))
"""
            D
            /\
           B  E
           /\  \
          A  C  G
                /
               F
"""

"""
深度优先
遍历规则：不断地沿着顶点的深度方向遍历。顶点的深度方向是指它的邻接点方向。
"""


def depth_tree(tree_node):
    """
    深度优先 遍历
    :param tree_node:
    :return:
    """
    if tree_node is not None:
        print(tree_node.val)
        if tree_node.left is not None:
            depth_tree(tree_node.left)
        if tree_node.right is not None:
            depth_tree(tree_node.right)


# depth_tree(T)
"""
D
B
A
C
E
G
F
"""

"""
广度优先
遍历规则：
1）先访问完当前顶点的所有邻接点。(应该看得出广度的意思)
2）先访问顶点的邻接点先于后访问顶点的邻接点被访问。
"""

from queue import Queue


def level_queue(tree_node):
    if tree_node is None:
        return
    q = Queue()
    q.put(tree_node)
    while q:
        node = q.get()
        print(node.val)
        if node.left is not None:
            q.put(node.left)
        if node.right is not None:
            q.put(node.right)


level_queue(T)
"""
D
B
E
A
C
G
F
"""

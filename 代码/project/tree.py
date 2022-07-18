"""
生成树
"""


class Tree:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left  # 左子树
        self.right = right  # 右子树


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


def pre_traverse(tree):
    """
    前序遍历 根 左 右（根节点排最先，然后同级先左后右）
    :param tree: 二叉树
    :return:
    """
    if tree is None:
        return
    print(tree.value)
    pre_traverse(tree.left)
    pre_traverse(tree.right)


print("前序遍历")
pre_traverse(T)
"""
前序排列原理
1. tree=Tree(D) print(D), D入栈【D】
2. tree=Tree(D).left=Tree(B) print(B), B入栈【D, B】
3. tree=Tree(B).left=Tree(A) print(A), A入栈【D, B, A】
4. tree=Tree(A).left=None, 没有进入递归，顺序执行 pre_traverse(tree.right)
5. tree=Tree(A).right=None, 也没有进入递归，此时 pre_traverse(A) 函数才会真正返回，A出栈【D, B】
6. A的上级调用函数为：pre_traverse(B.left)
"""


def mid_traverse(tree):
    """
    中序遍历 左根右（先左 后根 最后右）
    :param tree:
    :return:
    """
    if tree is None:
        return
    mid_traverse(tree.left)
    print(tree.value)
    mid_traverse(tree.right)


print("中序遍历")
mid_traverse(T)


def after_traverse(tree):
    """
    后序遍历 左右根（先左 后右 最后根）
    :param tree:
    :return:
    """
    if tree is None:
        return
    after_traverse(tree.left)
    after_traverse(tree.right)
    print(tree.value)


print("后序遍历")
after_traverse(T)

"""
分层打印二叉树
"""


def layered_print(tree):
    """
    分层打印二叉树
    :param tree:
    :return:
    """
    if not tree:
        return
    cur_layer = [tree]
    while cur_layer:
        layer_value = []
        next_layer = []
        for t in cur_layer:
            layer_value.append(t.value)
            if t.left:
                next_layer.append(t.left)
            if t.right:
                next_layer.append(t.right)
        print(layer_value)
        cur_layer = next_layer


print("分层打印")
layered_print(T)

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

"""
树模拟文件夹
"""


class Node:

    def __init__(self, name, ty="dir"):
        """

        :param name: 目录名称
        :param ty: 类型
        """
        self.name = name
        self.type = ty
        self.parent = None
        self.children = []

    def __repr__(self):
        """返回展示名称而非内存地址"""
        return self.name


class FileTree:

    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        """
        创建目录
        :param name: 新目录名称
        :return:
        """
        if name[-1] != "/":
            name += "/"
        # 创建该节点
        node = Node(name)
        # 为根目录添加当前节点
        self.now.children.append(node)

    def ls(self):
        """
        返回当前目录下的所有节点
        :return:
        """
        return self.now.children

    def cd(self, name):
        """
        进入指定目录

        :param name: 目录名称
        :return:
        """
        if name[-1] != "/":
            name += "/"
        # 判断是否为返回上一级
        if name == "../":
            self.now = self.now.parent
            return
        # 寻找到指定的目录
        for child in self.now.children:
            if child.name == name:
                self.now = child
                return
        # 没有查找的目录抛出异常
        raise ValueError("invalid dir")


tree = FileTree()
tree.mkdir("bin")
tree.mkdir("etc")

print("---", tree.ls())
tree.cd("etc")
print("---", tree.ls())

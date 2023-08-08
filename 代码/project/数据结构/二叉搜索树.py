class BinarySearchTree:

    def __init__(self, val, parent=None):
        self.val = val
        self.l_children = None
        self.r_children = None
        self.parent = parent


class BST:
    def __init__(self, li):
        self.root = None
        if li:
            for i in li:
                # self.root = self.insert_recursion(self.root, i)
                self.insert(i)

    def insert_recursion(self, node, val):
        """

        :param node: 当前节点
        :param val:当前值
        :return:
        """
        if not node:
            node = BinarySearchTree(val)
        # 左子树
        elif val < node.val:
            # 递归生成
            node.l_children = self.insert_recursion(node.l_children, val)
            # 关联当前节点与父节点
            node.l_children.parent = node
        # 右子树
        elif val > node.val:
            node.r_children = self.insert_recursion(node.r_children, val)
            node.r_children.parent = node
        return node

    def insert(self, val):
        """

        :param val: 当前值
        :return:
        """
        # 生成节点
        p = self.root
        if not p:
            self.root = BinarySearchTree(val)
            return
        while 1:
            # 左节点
            if val < p.val:
                # 左节点的第一个收否有值，无值进行创建
                if p.l_children:
                    p = p.l_children
                # 有值继续向下
                else:
                    p.l_children = BinarySearchTree(val)
                    p.l_children.parent = p
                    return
            elif val > p.val:
                if p.r_children:
                    p = p.r_children
                else:
                    p.r_children = BinarySearchTree(val)
                    p.r_children.parent = p
                    return
            else:
                return


tree = BST([4, 6, 7, 9, 2, 1, 3])


def pre_traverse(tree):
    """
    前序遍历 根 左 右（根节点排最先，然后同级先左后右）
    :param tree: 二叉树
    :return:
    """
    if tree is None:
        return
    print(tree.val, end=",")
    pre_traverse(tree.l_children)
    pre_traverse(tree.r_children)


pre_traverse(tree.root)
print("前序遍历")


def mid_traverse(tree):
    """
    中序遍历 左根右（先左 后根 最后右）
    :param tree:
    :return:
    """
    if tree is None:
        return
    mid_traverse(tree.l_children)
    print(tree.val, end=",")
    mid_traverse(tree.r_children)


mid_traverse(tree.root)
print("中序遍历")


def after_traverse(tree):
    """
    后序遍历 左右根（先左 后右 最后根）
    :param tree:
    :return:
    """
    if tree is None:
        return
    after_traverse(tree.l_children)
    after_traverse(tree.r_children)
    print(tree.val, end=",")


after_traverse(tree.root)
print("后序遍历")

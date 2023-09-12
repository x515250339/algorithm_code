"""
单链表
"""


class Linked:

    def __init__(self, item: int, next: int = None):
        self.item = item
        self.next = next


l = Linked(1, Linked(2, Linked(3, Linked(4))))

# print(l)
# print(l.item)
# print(l.next.item)
# print(l.next.next.item)

"""
单向翻转链表
"""


def list_reverse(head=None):
    if head is None:
        return None
    L, R, cur = None, None, head  # 左指针 右指针 游标
    while cur.next is not None:
        L = R  # 左侧指针指向以前右侧指针位置
        R = cur  # 右侧指针前进一位指向当前游标位置
        cur = cur.next  # 游标每次向前进一位
        R.next = L  # 右侧指针指向左侧实现反转
    cur.next = R  # 当跳出 while 循环时 cur(原链表最后一个元素) R(原链表倒数第二个元素)
    return cur


'''
原始链表：1 -> 2 -> 3 -> 4
反转链表：4 -> 3 -> 2 -> 1
'''
L = Linked(1)
L.next = Linked(2)
L.next.next = Linked(3)
L.next.next.next = Linked(4)
print(L.item)
print(L.next.item)
print(L.next.next.item)
l = list_reverse(L)
print(l.item)
print(l.next.item)
print(l.next.next.item)


def head_create_linked(li: list) -> Linked:
    """
    头插法

    :param li: 输入列表
    :return: type(Linked)
    """
    head = Linked(li[0])

    for cur in li[1:]:
        node = Linked(cur)
        node.next = head
        head = node
    return head


def print_linked(linked: list) -> None:
    if linked:
        print(linked.item, end=",")
        print_linked(linked.next)


def tail_create_linked(li: list) -> Linked:
    """
    尾插法

    :param li: 输入列表
    :return: type(Linked)
    """
    head = Linked(li[0])
    tail = head

    for cur in li[1:]:
        node = Linked(cur)
        tail.next = node
        tail = node

    return head


node = head_create_linked([1, 2, 3])
print_linked(node)
print()
node = tail_create_linked([1, 2, 3])
print_linked(node)

class LinkedList:
    class Node:
        """
        链表
        """

        def __init__(self, item):
            self.item = item
            self.next = None

    class LinkListIterator:
        """
        链表迭代器
        """

        def __init__(self, node):
            self.node = node

        def __next__(self):
            """
            返回下一节点
            """
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration

        def __iter__(self):
            """
            返回本身
            """
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)

    def append(self, obj):
        """
        添加元素
        """
        s = LinkedList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        """
        追加元素
        """
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        """
        查找元素
        """
        for n in self:
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):
        """迭代"""
        return self.LinkListIterator(self.head)

    def __repr__(self):
        """输出值"""
        return "<<" + ",".join(map(str, self)) + ">>"


class HashTable:
    def __init__(self, size: int = 101):
        """构建大小"""
        self.size = size
        self.T = [LinkedList() for i in range(self.size)]

    def h(self, k):
        """hash函数"""
        return k % self.size

    def insert(self, k):
        """插入"""
        i = self.h(k)
        if self.find(k):
            print("Duplicated hash table")
        else:
            self.T[i].append(k)

    def find(self, k):
        """查找"""
        i = self.h(k)
        return self.T[i].find(k)


hash_table = HashTable()
hash_table.insert(0)
hash_table.insert(1)
hash_table.insert(3)
hash_table.insert(102)
hash_table.insert(508)
print(",".join(map(str, hash_table.T)))

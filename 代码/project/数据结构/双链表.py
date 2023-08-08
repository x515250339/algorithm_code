class DoubleLinked:

    def __init__(self, item: int = None, next: int = None, prior: int = None):
        self.next = next
        self.item = item
        self.prior = prior


class DoubleLinkedFunc:

    def __init__(self):
        self.lt = [1, 2, 3, 4]

    def create_linked(self):
        """
        插入

        :return:
        """
        node = DoubleLinked(self.lt[0])
        tail = node
        for cur in self.lt[1:]:
            cur_node = DoubleLinked(cur)
            tail.next = cur_node
            cur_node.prior = node.item
            tail = cur_node
        return node

    def delete_linked(self):
        """
        删除

        :return:
        """
        node = self.create_linked()
        p = node.next
        node.next = p.next
        p.next.prior = node
        del p
        return node

    def print_linked(self, linked):
        if linked:
            print(linked.item, end=",")
            self.print_linked(linked.next)


f = DoubleLinkedFunc()
linked = f.create_linked()
f.print_linked(linked)
linked = f.delete_linked()
print()
f.print_linked(linked)

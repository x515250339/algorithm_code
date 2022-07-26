"""
["CQueue","appendTail","deleteHead","deleteHead"]
这一行表示每一行代码的操作

[[],[3],[],[]]
这个表示每一行代码操作后对应的结果

举例：
CQueue 表示新建一个CQueue对象，对应的结果为[]。
appendTail 表示执行一个appendTail()操作，对应要被操作的元素为3
deleteHead 表示执行一个deleteHead操作，对应的结果为[]
deleteHead 表示执行一个deleteHead操作，对应的结果为[]

以上的输入其实是一个代码执行的步骤描述与其对应结果或操作。
并不是说，上面的“输入”表示的输入程序验证的数据.
"""


class CQueue:

    def __init__(self):
        self.add_list = []
        self.del_list = []

    def appendTail(self, value: int) -> None:
        self.add_list.append(value)

    def deleteHead(self) -> int:
        if self.del_list:
            return self.del_list.pop()
        if not self.add_list:
            return -1
        while self.add_list:
            self.del_list.append(self.add_list.pop())
        return self.del_list.pop()


# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()


[[], [3], [], []]

obj = CQueue()
print(obj.deleteHead())
obj.appendTail(5)
obj.appendTail(2)
print(obj.deleteHead())
print(obj.deleteHead())

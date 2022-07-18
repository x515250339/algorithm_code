class Stack(object):

    def __init__(self):
        self.stack = []

    def push(self, item):
        """
        入栈
        :param item:
        :return:
        """
        self.stack.append(item)

    def get_top(self):
        """
        获取栈顶元素
        :return:
        """
        return self.stack[-1]

    def pop(self):
        """
        出栈
        :return:
        """
        return self.stack.pop()


class MyStack:

    def __init__(self):
        self.s = []

    def push(self, x: int) -> None:
        self.s.append(x)

    def pop(self) -> int:
        return self.s.pop()

    def size(self) -> int:
        return len(self.s)

    def empty(self) -> bool:
        return not bool(self.s)


stack = MyStack()


def trans_from(num: int) -> str:
    while num != 0:
        re_main = num % 2
        print("re_main", re_main)
        num = int(num / 2)
        print("num", num)
        stack.push(re_main)
    s = ""
    while not stack.empty():
        s += str(stack.pop())
    return s


if __name__ == '__main__':
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # print(s.stack)
    # print(s.get_top())
    # print(s.pop())
    # print(s.get_top())
    print(trans_from(12))

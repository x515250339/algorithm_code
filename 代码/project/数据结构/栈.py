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


maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],

]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y + 1),
    lambda x, y: (x, y - 1),
]


def maze_path(x1: int, y1: int, x2: int, y2: int):
    """
    走出迷宫，采用dfs深度优先搜索，也叫回溯法，如果当前位置不可继续前进，那么则回退到上一个位置，重复如此。
    时间复杂度: O(n)
    空间复杂度: O(n)

    :param x1: 入口x
    :param y1: 入口y
    :param x2: 出口x
    :param y2: 出口y
    :return: [] 踪迹
    """
    stack = [(x1, y1)]
    while stack:
        cur_node = stack[-1]
        for d in dirs:
            next_node = d(cur_node[0], cur_node[1])
            if next_node[0] == x2 and next_node[1] == y2:
                return stack
            if maze[next_node[0]][next_node[1]] == 0:
                stack.append(next_node)
                maze[next_node[0]][next_node[1]] = 2
                break
        else:
            maze[next_node[0]][next_node[1]] = 2
            stack.pop()
    return False


if __name__ == '__main__':
    print(maze_path(1, 1, 8, 8))
    # s = Stack()
    # s.push(1)
    # s.push(2)
    # print(s.stack)
    # print(s.get_top())
    # print(s.pop())
    # print(s.get_top())
    # print(trans_from(12))

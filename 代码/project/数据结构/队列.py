from queue import Queue

# 1. 基本FIFO队列  先进先出 FIFO即First in First Out,先进先出
# 2. maxsize设置队列中，数据上限，小于或等于0则不限制，容器中大于这个数则阻塞，直到队列中的数据被消掉
q = Queue(maxsize=0)

# 3. 写入队列数据
q.put(0)
q.put(1)
q.put(2)

# 4. 输出当前队列所有数据
print(q.queue)

# 5. 删除队列数据，并返回该数据
q.get()

# 6. 输也所有队列数据
print(q.queue)

"""
手写 Queue
"""


class Queue:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        return self.q.pop(0)

    def is_empty(self) -> bool:
        return not bool(self.q)

    def size(self) -> int:
        return len(self.q)


if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    q.push(3)
    print(q.pop())
    print(q.pop())
    print(q.is_empty())
    print(q.size())

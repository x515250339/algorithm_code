from abc import ABCMeta, abstractmethod


class Handler(metaclass=ABCMeta):

    @abstractmethod
    def handle_leave(self, day):
        pass


class GeneralManager(Handler):

    def handle_leave(self, day):
        if day >= 10:
            print("总经理准假 %d" % day)
        else:
            print("你还是离职吧")


class DepartmentManager(Handler):

    def __init__(self):
        self.next = GeneralManager()

    def handle_leave(self, day):
        if day >= 5:
            print("部门经理准假 %d" % day)
        else:
            print("部门经理无权限")
            self.next.handle_leave(day)


class ProjectManager(Handler):

    def __init__(self):
        self.next = DepartmentManager()

    def handle_leave(self, day):
        if day >= 3:
            print("项目经理准假 %d" % day)
        else:
            print("项目经理无权限")
            self.next.handle_leave(day)


day = 4
p = ProjectManager()
p.handle_leave(day)


# 处理者抽象类
class Handler:
    def __init__(self):
        self.successor = None

    def set_successor(self, successor):
        self.successor = successor

    def handle_request(self, request):
        pass


# 具体处理者A
class ConcreteHandlerA(Handler):
    def handle_request(self, request):
        if request == 'A':
            print("ConcreteHandlerA 处理请求")
        elif self.successor is not None:
            self.successor.handle_request(request)


# 具体处理者B
class ConcreteHandlerB(Handler):
    def handle_request(self, request):
        if request == 'B':
            print("ConcreteHandlerB 处理请求")
        elif self.successor is not None:
            self.successor.handle_request(request)


# 具体处理者C
class ConcreteHandlerC(Handler):
    def handle_request(self, request):
        if request == 'C':
            print("ConcreteHandlerC 处理请求")
        elif self.successor is not None:
            self.successor.handle_request(request)


# 客户端代码
handlerA = ConcreteHandlerA()
handlerB = ConcreteHandlerB()
handlerC = ConcreteHandlerC()

handlerA.set_successor(handlerB)
handlerB.set_successor(handlerC)

handlerA.handle_request('B')

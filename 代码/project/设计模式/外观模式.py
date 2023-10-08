# 子系统A
class SubsystemA:
    def operationA(self):
        print("Subsystem A operation")


# 子系统B
class SubsystemB:
    def operationB(self):
        print("Subsystem B operation")


# 外观类
class Facade:
    def __init__(self):
        self.subsystemA = SubsystemA()
        self.subsystemB = SubsystemB()

    def operation(self):
        self.subsystemA.operationA()
        self.subsystemB.operationB()


# 客户端代码
facade = Facade()
facade.operation()

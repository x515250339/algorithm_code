from abc import ABC, abstractmethod


# 组件接口
class Component(ABC):
    @abstractmethod
    def operation(self):
        pass


# 叶子类
class Leaf(Component):
    def operation(self):
        print("执行叶子操作")


# 容器类
class Composite(Component):
    def __init__(self):
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def operation(self):
        print("执行容器操作")
        for child in self.children:
            child.operation()


# 使用组合模式
leaf1 = Leaf()
leaf2 = Leaf()

composite1 = Composite()
composite1.add(leaf1)
composite1.add(leaf2)

leaf3 = Leaf()

composite2 = Composite()
composite2.add(leaf3)
composite2.add(composite1)

composite2.operation()

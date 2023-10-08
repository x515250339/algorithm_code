from abc import ABC, abstractmethod


# 实现部分的接口
class Shape(ABC):
    def __init__(self, color):
        self.color = color

    @abstractmethod
    def draw(self):
        pass


# 实现部分的接口
class Color(ABC):
    @abstractmethod
    def paint(self, shape):
        pass


# 长方形
class Rectangle(Shape):
    name = "长方形"

    def draw(self):
        self.color.paint(self)


# 圆形
class Round(Shape):
    name = "圆形"

    def draw(self):
        self.color.paint(self)


class Red(Color):
    def paint(self, shape):
        print("红色的 %s" % shape.name)


class Green(Color):
    def paint(self, shape):
        print("绿色的 %s" % shape.name)


r = Rectangle(Red())
g = Round(Green())
r.draw()
g.draw()

from abc import ABC, abstractmethod


# 实现部分的接口
class Implementor(ABC):
    @abstractmethod
    def operation_implementation(self):
        pass


# 具体实现部分A
class ConcreteImplementorA(Implementor):
    def operation_implementation(self):
        print("Concrete Implementor A operation")


# 具体实现部分B
class ConcreteImplementorB(Implementor):
    def operation_implementation(self):
        print("Concrete Implementor B operation")


# 抽象部分的接口
class Abstraction(ABC):
    def __init__(self, implementor):
        self.implementor = implementor

    @abstractmethod
    def operation(self):
        pass


# 具体抽象部分A
class ConcreteAbstractionA(Abstraction):
    def operation(self):
        print("Concrete Abstraction A operation")
        self.implementor.operation_implementation()


# 具体抽象部分B
class ConcreteAbstractionB(Abstraction):
    def operation(self):
        print("Concrete Abstraction B operation")
        self.implementor.operation_implementation()


# 使用桥模式
implementor_a = ConcreteImplementorA()
abstraction_a = ConcreteAbstractionA(implementor_a)
abstraction_a.operation()

implementor_b = ConcreteImplementorB()
abstraction_b = ConcreteAbstractionB(implementor_b)
abstraction_b.operation()

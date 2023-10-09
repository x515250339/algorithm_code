from time import sleep
from abc import ABCMeta, abstractmethod


class Window(metaclass=ABCMeta):

    def start(self):
        pass

    def repaint(self):
        pass

    def stop(self):
        pass

    def run(self):
        self.start()
        while True:
            try:
                self.repaint()
                sleep(1)
            except KeyboardInterrupt:
                break
        self.stop()


class MyWindows(Window):
    def __init__(self, msg):
        self.msg = msg

    def start(self):
        print("窗口开始运行")

    def stop(self):
        print("窗口结束运行")

    def repaint(self):
        print(self.msg)


MyWindows("hello -----").run()


# 抽象类
class AbstractClass:
    def template_method(self):
        self.step1()
        self.step2()

    def step1(self):
        pass

    def step2(self):
        pass


# 具体类1
class ConcreteClass1(AbstractClass):
    def step1(self):
        print("ConcreteClass1 - Step 1")

    def step2(self):
        print("ConcreteClass1 - Step 2")


# 具体类2
class ConcreteClass2(AbstractClass):
    def step1(self):
        print("ConcreteClass2 - Step 1")

    def step2(self):
        print("ConcreteClass2 - Step 2")


concrete1 = ConcreteClass1()
concrete1.template_method()
"""
输出:
ConcreteClass1 - Step 1
ConcreteClass1 - Step 2
"""

concrete2 = ConcreteClass2()
concrete2.template_method()
"""
输出:
ConcreteClass2 - Step 1
ConcreteClass2 - Step 2
"""

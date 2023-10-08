from abc import abstractmethod, ABCMeta


class Observer(metaclass=ABCMeta):

    def update(self, notices):
        pass


# 具体主题
class Notices:
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


# 观察者接口
class Observer:
    def update(self):
        pass


# 具体观察者A
class ConcreteObserverA(Observer):
    def update(self):
        print("ConcreteObserverA 收到通知并进行更新")


# 具体观察者B
class ConcreteObserverB(Observer):
    def update(self):
        print("ConcreteObserverB 收到通知并进行更新")


# 客户端代码
subject = ConcreteSubject()
observerA = ConcreteObserverA()
observerB = ConcreteObserverB()

subject.attach(observerA)
subject.attach(observerB)

subject.notify()


# 主题接口
class Subject:
    def attach(self, observer):
        pass

    def detach(self, observer):
        pass

    def notify(self):
        pass


# 具体主题
class ConcreteSubject(Subject):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()


# 观察者接口
class Observer:
    def update(self):
        pass


# 具体观察者A
class ConcreteObserverA(Observer):
    def update(self):
        print("ConcreteObserverA 收到通知并进行更新")


# 具体观察者B
class ConcreteObserverB(Observer):
    def update(self):
        print("ConcreteObserverB 收到通知并进行更新")


# 客户端代码
subject = ConcreteSubject()
observerA = ConcreteObserverA()
observerB = ConcreteObserverB()

subject.attach(observerA)
subject.attach(observerB)

subject.notify()

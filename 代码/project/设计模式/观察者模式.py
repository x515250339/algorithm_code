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
            observer.update(self)


# 观察者接口
class StaffNotice(Notices):

    def __init__(self, company_info=None):
        super().__init__()
        self.__company_info = company_info

    @property
    def company_info(self):
        return self.__company_info

    @company_info.setter
    def company_info(self, info):
        self.__company_info = info
        self.notify()


class Staff(Observer):

    def __init__(self):
        self.company_info = None

    def update(self, notices):
        self.company_info = notices.company_info


notice = StaffNotice("初始化公司信息")
s1 = Staff()
s2 = Staff()
notice.attach(s1)
notice.attach(s2)
notice.company_info = "公司今年业绩很好"
print(s1.company_info)
print(s2.company_info)
notice.detach(s2)
notice.company_info = "公司明年业绩也很好"
print(s1.company_info)
print(s2.company_info)


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

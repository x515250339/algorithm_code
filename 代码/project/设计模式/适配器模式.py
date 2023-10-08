# 目标接口
class Target:
    def request(self):
        raise NotImplementedError


# 对象适配器
class Adapter(Target):
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        # 调用现有类的方法进行适配
        self.adaptee.specific_request()


class Adaptee:
    def specific_request(self):
        print("Adaptee's specific request")


# 类适配器
class NewAdaptee(Target, Adaptee):
    def request(self):
        self.specific_request()


# 使用适配器
adapter = Adapter(Adaptee())
adapter.request()
# 使用适配器
adapter2 = NewAdaptee()
adapter2.request()

from abc import ABCMeta, abstractmethod


# 定义初始类
class PayCommon(metaclass=ABCMeta):

    @abstractmethod
    def draw(self, money):
        pass


# 实现支付宝支付
class AliPay(PayCommon):
    def draw(self, money):
        print("支付宝支付 % d" % money)


# 实现微信支付
class WeChatPay(PayCommon):
    def draw(self, money):
        print("微信支付 % d" % money)


# 定义形状工厂类
class ShapeFactory:
    def pay(self, shape_type):
        if shape_type == "ali":
            return AliPay()
        elif shape_type == "wechat":
            return WeChatPay()
        else:
            raise ValueError("不支持的支付类型")


# 客户端代码
if __name__ == "__main__":
    factory = ShapeFactory()

    circle = factory.pay("ali")
    circle.draw(100)

    rectangle = factory.pay("wechat")
    rectangle.draw(10)

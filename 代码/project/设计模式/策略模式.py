from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):

    @abstractmethod
    def execute(self, data):
        pass


class FastStrategy(Strategy):

    def execute(self, data):
        print("较快的策略%s", data)


class SlowStrategy(Strategy):

    def execute(self, data):
        print("较慢的策略%s", data)


class Context:

    def __init__(self, data, strategy):
        self.data = data
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def do_strategy(self):
        self.strategy.execute(self.data)


data = "[....]"
s1 = FastStrategy()
s2 = SlowStrategy()
context = Context(data, s1)
context.do_strategy()
context.set_strategy(s2)
context.do_strategy()


# ---------------------------------------------------------------


# 定义策略接口
class PaymentStrategy:
    def pay(self, amount):
        pass


# 具体策略类1：信用卡支付
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with Credit Card")


# 具体策略类2：支付宝支付
class AlipayPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paid ${amount} with Alipay")


# 上下文类
class ShoppingCart:
    def __init__(self, payment_strategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount):
        self.payment_strategy.pay(amount)


# 客户端代码
if __name__ == "__main__":
    credit_card_payment = CreditCardPayment()
    alipay_payment = AlipayPayment()

    cart1 = ShoppingCart(credit_card_payment)
    cart1.checkout(100.0)  # 输出 "Paid $100.0 with Credit Card"

    cart2 = ShoppingCart(alipay_payment)
    cart2.checkout(50.0)  # 输出 "Paid $50.0 with Alipay"

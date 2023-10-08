from abc import ABC, abstractmethod


# 定义支付方式的抽象基类
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# 实现信用卡支付类
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"使用信用卡支付 ${amount}")


# 实现支付宝支付类
class AlipayPayment(PaymentMethod):
    def pay(self, amount):
        print(f"使用支付宝支付 ${amount}")


# 定义支付方式工厂的抽象基类
class PaymentFactory(ABC):
    @abstractmethod
    def create_payment_method(self):
        pass


# 实现信用卡支付工厂
class CreditCardPaymentFactory(PaymentFactory):
    def create_payment_method(self):
        return CreditCardPayment()


# 实现支付宝支付工厂
class AlipayPaymentFactory(PaymentFactory):
    def create_payment_method(self):
        return AlipayPayment()


# 客户端代码
if __name__ == "__main__":
    credit_card_factory = CreditCardPaymentFactory()
    credit_card_payment = credit_card_factory.create_payment_method()
    credit_card_payment.pay(100.0)

    alipay_factory = AlipayPaymentFactory()
    alipay_payment = alipay_factory.create_payment_method()
    alipay_payment.pay(50.0)

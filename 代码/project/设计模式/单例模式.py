from functools import wraps


def test_func(func):
    _instance = {}

    @wraps(func)
    def inner(*args, **kwargs):
        if func not in _instance:
            _instance[func] = func()
        return _instance[func]

    return inner


class TestClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if TestClass._instance:
            return TestClass._instance
        else:
            TestClass._instance = object.__new__(cls, *args, **kwargs)
            return TestClass._instance


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "_instance"):
            cls._instance = super(Singleton, cls).__new__(cls)


class MyClass(Singleton):
    def __init__(self):
        pass


@test_func
class MyClass2:

    def __init__(self):
        pass


if __name__ == '__main__':
    t1 = TestClass()
    t2 = TestClass()
    print(t1 is t2)
    t3 = MyClass()
    t4 = MyClass()
    print(t3 is t4)
    t5 = MyClass2()
    t6 = MyClass2()
    print(t5 is t6)

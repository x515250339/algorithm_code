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


if __name__ == '__main__':
    t1 = TestClass()
    t2 = TestClass()
    print(t1 == t2)

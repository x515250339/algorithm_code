from abc import ABCMeta, abstractmethod


class Subject:

    @abstractmethod
    def get_content(self):
        pass

    @abstractmethod
    def set_content(self, content):
        pass


class RealSubject(Subject):

    def __init__(self, file_name):
        self.file_name = file_name
        print("读取文件内容")
        with open(file_name, "r", encoding="utf-8") as f:
            self.content = f.read()

    def get_content(self):
        print(self.content)
        return self.content

    def set_content(self, content):
        with open(self.file_name, "rw", encoding="utf-8") as f:
            f.write(content)


class VirtualSubject(Subject):

    def __init__(self, file_name):
        self.file_name = file_name
        self.subject = None

    def get_content(self):
        if not self.subject:
            self.subject = RealSubject(self.file_name)
        return self.subject.get_content()

    # def set_content(self, content):
    #     if not self.subject:
    #         self.subject = RealSubject(self.file_name)
    #     return self.subject.set_content(content)

    # 可以进行加密
    def set_content(self, content):
        raise PermissionError("no permission")


r = RealSubject("test.txt")

v = VirtualSubject("test.txt")
v.get_content()


# 抽象主题
class Subject:
    def request(self):
        pass


# 真实主题
class RealSubject(Subject):
    def request(self):
        print("执行真实主题的请求")


# 代理
class Proxy(Subject):
    def __init__(self):
        self.real_subject = RealSubject()

    def request(self):
        # 在访问真实主题前可以添加额外的逻辑
        print("执行代理的请求")
        self.real_subject.request()
        # 在访问真实主题后可以添加额外的逻辑


# 客户端代码
subject = Proxy()
subject.request()

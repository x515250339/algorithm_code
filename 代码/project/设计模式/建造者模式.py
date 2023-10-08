from abc import ABC, abstractmethod


# 定义电脑抽象基类
class Computer(ABC):
    def __init__(self):
        self.cpu = None
        self.memory = None
        self.hard_drive = None
        self.graphics_card = None
        self.meat = None

    @abstractmethod
    def __str__(self):
        pass


# 定义电脑建造者接口
class ComputerBuilder(ABC):
    @abstractmethod
    def set_cpu(self, cpu):
        pass

    @abstractmethod
    def set_memory(self, memory):
        pass

    @abstractmethod
    def set_hard_drive(self, hard_drive):
        pass

    @abstractmethod
    def set_graphics_card(self, graphics_card):
        pass

    @abstractmethod
    def set_meat(self, meat):
        pass

    @abstractmethod
    def build(self):
        pass


# 具体的电脑类
class ConcreteComputer(Computer):
    def __str__(self):
        return f"CPU: {self.cpu}, Memory: {self.memory}, Hard Drive: {self.hard_drive}, Graphics Card: {self.graphics_card}, Meat: {self.meat}"


# 具体的电脑建造者
class ConcreteComputerBuilder(ComputerBuilder):
    def __init__(self):
        self.computer = ConcreteComputer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu

    def set_memory(self, memory):
        self.computer.memory = memory

    def set_hard_drive(self, hard_drive):
        self.computer.hard_drive = hard_drive

    def set_graphics_card(self, graphics_card):
        self.computer.graphics_card = graphics_card

    def set_meat(self, meat):
        self.computer.meat = meat

    def build(self):
        return self.computer


# 定义电脑指导者
class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_cpu("Intel Core i7")
        self.builder.set_memory("16GB")
        self.builder.set_hard_drive("1TB SSD")
        self.builder.set_graphics_card("NVIDIA GeForce RTX 3080")
        self.builder.set_meat("Beef")
        return self.builder.build()


# 定义高端电脑指导者
class ComputerDirectorHighEnd:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.set_cpu("Intel Core i9")
        self.builder.set_memory("64GB")
        self.builder.set_hard_drive("10TB SSD")
        self.builder.set_graphics_card("NVIDIA GeForce RTX 4090Ti")
        self.builder.set_meat("Beef")
        return self.builder.build()


# 客户端代码
if __name__ == "__main__":
    builder = ConcreteComputerBuilder()
    director = ComputerDirector(builder)

    computer = director.construct()

    print("构建的电脑信息:")
    print(computer)
    director = ComputerDirectorHighEnd(builder)

    computer = director.construct()
    print("构建的电脑信息:")
    print(computer)

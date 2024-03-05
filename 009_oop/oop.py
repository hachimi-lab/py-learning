"""
面向对象编程
属性和方法以_开头的是受保护的，外部可以访问但不建议
属性和方法以__开头的是私有的，外部无法访问
"""
from abc import abstractmethod, ABC


# abstract base class, like interface in Java
class Animal(ABC):
    @abstractmethod
    def walk(self):
        pass


# base class
class Cat(Animal):
    def __init__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'

    def walk(self):
        print(f'{self.name} is walking')


# derived class
class ShortCat(Cat):
    # 有默认值的参数必须放在没有默认值的参数后面
    def __init__(self, age: int, name: str = '咪咪'):
        super().__init__(name, age)
        self.public_attribute = "I'm public!"  # 公有属性
        self._protected_attribute = "I'm protected!"  # 受保护属性
        self.__private_attribute = "I'm private!"  # 私有属性

    @staticmethod
    def just_meow():
        print('Meow!')

    def walk(self):
        print(f'{self.name} is walking like a cat')


# 通过类名调用静态方法
ShortCat.just_meow()

# 实例化对象
cat = ShortCat(3, 'Kitty')
print(cat)
cat.walk()

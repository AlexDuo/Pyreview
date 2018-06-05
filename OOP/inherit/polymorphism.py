# Author: Real   
# CreateTime 5/31/2018-12:25 PM   
# IDE: PyCharm

# 多态 （目的：接口的重用）：是允许将父对象设置成为与一个货更多的他的子对象相等的技术，赋值后，父对象就可以根据当前赋值给他的子对象的特性以不同的方式运作
# 简单的说，就是允许将子类类型的指针赋值给父类类型的指针


# 核心原则，同一个原则多种实现

class Animal:
    def __init__(self,name):
        self.name =name

    def talk(self):
        pass


class Cat(Animal):
    def talk(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return 'Woof Woof!'
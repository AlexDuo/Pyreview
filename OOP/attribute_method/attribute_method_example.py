# Author: Real   
# CreateTime 5/31/2018-1:35 PM   
# IDE: PyCharm

class Dog():
    name = 'tommi'

    def __init__(self,name):
        self.name = name
        self.__food = None

    @property
    def eat(self):  #属性方法的修饰词的作用是，把一个方法变成一个静态属性
        print('%s is eating %s'%(self.name, self.__food))

    @eat.setter
    def eat(self,food):
        print('set attribute %s to attribute method eat'%food)
        self.__food = food

    # @eat.deleter
    def eat(self): #属性方法的删除
        del self.__food
        print('private attribute has already been deleted')


d = Dog('Pigi')


d.eat

d.eat = 'bone'

d.eat

# 属性方法是没有办法删除的

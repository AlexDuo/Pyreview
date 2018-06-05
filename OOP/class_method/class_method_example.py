# Author: Real   
# CreateTime 5/31/2018-1:26 PM   
# IDE: PyCharm

class Dog():
    name = 'tommi'

    def __init__(self,name):
        self.name = name

    @classmethod #类方法只能访问类变量，不能访问实例变量
    def eat(self,food):
        print('%s is eating %s'%(self.name,food))


d = Dog('Pigi')

d.eat('happy bone')
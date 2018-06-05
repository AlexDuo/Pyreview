# Author: Real   
# CreateTime 5/31/2018-1:17 PM   
# IDE: PyCharm

# 静态方法只是名义上归类管理，实际上静态方法不能访问勒种的任何属性和方法。
class Dog():

    def __init__(self,name):
        self.name = name

    @staticmethod #静态方法实际上与类没有关系，如果把类中的一个方法变成静态方法，相当于切断这个方法与类的关系。唯一的不同是他需要用类名去调用
    def eat(self,food):
        print('%s is eating %s'%(self.name,food))


d = Dog('Pigi')

d.eat('happy bone')
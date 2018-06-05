# Author: Real   
# CreateTime 5/31/2018-9:05 AM   
# IDE: PyCharm

# 继承就是为了提高代码的利用率
# class People():  经典类

# 在python2中经典类的继承策略是按照深度优先顺序来进行继承的，新式类是按照广度优先进行继承的。
# 在python3中经典类和新式类都是按照广度优先顺序进行继承的


class People(object): #新式类   经典类和新式类的区别主要体现在多继承上  Java不支持多继承，python支持多继承

    def __init__(self,name,age):
        self.name = name
        self.age =age


    def eat(self):
        print('%s is eating'%self.name)

    def talk(self):
        print('%s is talking'%self.name)




class Relation(object):
    def makefriends(self,obj):
        print('%s is making friends with %s'%(self.name,obj.name))





class Man(People,Relation):
    def __init__(self,name,age,property): #子类也可以重构父类的构造函数，使得子类在初始化的时候有一些额外的属性，这个时候需要声明父类原有的属性
        # People.__init__(self,name,age)#并且调用父类的构造函数
        super(Man, self).__init__(name,age)
        self.property = property #追加指向新的属性即可

    def running(self): #在父类的基础之上追加新的方法

        print('%s is running'%self.name)

    def eat(self): # 重构父类的方法
        People.eat(self)
        print('%s eat more than others'% self.name)





m1 = Man('duo',27,2000000000)

m2 = Man('Guojun',60,2000000000)

m1.eat()

m1.running()

m1.makefriends(m2)
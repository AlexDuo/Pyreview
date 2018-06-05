# Author: Real   
# CreateTime 5/30/2018-10:19 PM   
# IDE: PyCharm

# 面向对象三大特性： 继承， 封装， 多态
class example:
    def __init__(self,name,age,sex):
        self.name = name
        self.age = age
        self.__sex = sex # 通过在类的属性前追加 __使这个属性变成私有属性，实例化之后实例的这个属性将不能够被访问。


    def showsex(self):

        print('sex is %s'%self.__sex) #对外提供方法进行访问，但是不可修改

    def __privatefunc(self): #私有方法和私有属性定义的方法是一样的
        print('this is a privatefunc')



e1 = example('duo',27,'M')


print(e1.name)

e1.showsex()

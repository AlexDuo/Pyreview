# Author: Real   
# CreateTime 5/31/2018-4:27 PM   
# IDE: PyCharm

def __init__(self,name,age):
    self.name = name
    self.age = age


def func(self):
    print('hello %s, your age is %s'%(self.name,self.age))


class1 = type('instance1',(object,),{'func':func,
                                     '__init__':__init__}) #通过此语句就将 class1变成了一个类

instance1 = class1("Duo Zhang",22)

print(type(class1))

# 我们称type 为类的类

instance1.func()
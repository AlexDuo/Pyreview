# Author: Real   
# CreateTime 5/31/2018-7:47 PM   
# IDE: PyCharm

# 反射就是通过字符串映射或者修改程序运行时的状态、属性、方法
# hasattr 就是判断一个对象是否有对与字符串同名的方法
# getattr 根据字符串去获取obj对象里对应方法的内存地址




class Dog(object):

    def __init__(self,name):
        self.name = name

    def eat(self,food):
        print('%s is eating %s'%(self.name,food))


def additional_func(self):
    print('this is an additional function, it will be added into the instance when setattr function is called by %s'%self.name)



d1 = Dog('Tommi')

choice = input("please input the method you want to choose").strip()


if hasattr(d1,choice):
    func = getattr(d1,choice)
    func('happy bone ')
else:
    setattr(d1,choice,additional_func)
    func2 = getattr(d1,choice)
    func2(d1)

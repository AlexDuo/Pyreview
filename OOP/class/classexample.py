# Author: Real   
# CreateTime 5/30/2018-7:28 PM   
# IDE: PyCharm


class dog:
    def __init__(self,name):# __init__ 是python类的构造函数，作用是在一个类实例化的时候做一些初始化的工作
        self.name =name
    def bulk(self):
        print('%swangwang'%self.name)



d1 = dog('dog1')


d1.bulk()
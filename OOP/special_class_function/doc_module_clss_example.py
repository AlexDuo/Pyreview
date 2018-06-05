# Author: Real   
# CreateTime 5/31/2018-3:13 PM   
# IDE: PyCharm

class Flight(object):
    '''
        this class is used to describe Flight!
    '''
    def __init__(self, flight_name):
        self.flight_name = flight_name

    def checking_status(self):#这里模拟的系统内部查询航班信息的方法
        print("system is checking %s's flight status" % self.flight_name)
        return 1
    @property
    def flight_status(self):
        status = self.checking_status()
        if status == 1:
            print("flight has been arrived")
        elif status == 2:
            print("flight has been canceled")
        elif status == 3:
            print("can't get flight's info, please check it up latter...")


    def __call__(self, *args, **kwargs):  #可以将已经实例化的实例再度调用并且接收传入值
        print('running call from instance',args,kwargs)

    def __str__(self): #当我们实例了很对对象的时候，当我们调用或者传入一个对象，通常显示的实例的内存地址并不能很好的帮助我们区分，这个就是自定义对象的打印显示

        return '<obj:%s>'%self.flight_name


#
f1 = Flight('UA985')
# #
# # print(Flight.__doc__) #doc 方法会打印这个类的描述信息
# #
# # print(Flight.__module__) # 输出调用者所使用的模块的路径
#
# print(f1.__class__)
#
# f1(name='duo zhang',role = 'manager')
#
# print(f1.__dict__)

# print(Flight.__dict__) #以字典的形式把一个类中所有的属性，方法，包括一些内置的对象打印出来

print(f1)



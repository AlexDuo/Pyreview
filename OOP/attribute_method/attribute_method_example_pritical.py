# Author: Real   
# CreateTime 5/31/2018-2:48 PM   
# IDE: PyCharm

class Flight(object):
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



f1 = Flight('UA985')

# 航空公司只需要对外提供航班的查询接口,并不需要,也不安全为用户提供查询的方法,这个时候属性方法就变得很有必要
f1.flight_status



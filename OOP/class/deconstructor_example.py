# Author: Real   
# CreateTime 5/30/2018-10:06 PM   
# IDE: PyCharm


# 构造函数是constructor，析构函数是deconstructor
# 析构函数是在实例释放和销毁的时候执行的，通常用于做一些收尾工作，如关闭一些建立数据库连接使用的临时文件


class textexample():
    def __init__(self,name):
        self.name = name



    # 析构函数会在实例被消除的时候执行，比如删除一个实例的时候
    def __del__(self):
        print('%s was deleted'%self.name)



ex1 = textexample('new example')


del ex1


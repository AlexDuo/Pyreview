# Author: Real   
# CreateTime 5/31/2018-4:36 PM   
# IDE: PyCharm


class MyType(type): #此处还有待局

    def __init__(self, what, base=None, dict=None):
        print("--MyType-- __init__")
        super(MyType, self).__init__(what, base, dict)

    def __call__(self, *args, **kwargs):
        print('--MyType-- __call__')
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, **kwargs)


class example(object):
    __metaclass__ = MyType

    def __init__(self, name):
        self.name = name
        print('--example-- __init__')

    def __new__(cls, *args, **kwargs): #实例化example类的时候 __new__ 会在 __init__ 之前执行
        print('--example-- __new__')
        return object.__new__(cls) #注释掉这句之后 __init__ 构造函数将不会被执行，这意味着实例并没有被真正创建
        # 所以通过这个例子我们知道 实例化过程是通过  __new__ 方法来实现的
        # __new__ 里面的 cls 其实是和 self 起到的一样的作用, cls是一个形参，它用来接受你要创建的对象，在这个例子中就是 example 类

instance1 = example("Duo Zhang")

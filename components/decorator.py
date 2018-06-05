# 装饰器本质是函数
# 它的功能是用来装饰其他函数，即为其他函数添加附加功能

# 装饰器的原则：
#     1. 不能修改被装饰函数的源代码
#     2. 不能修改被修饰函数的调用方式

import time

# def decorator(function):
#     def decorate(*args,**kwargs):
#         start_time = time.time()
#         function(*args,**kwargs)
#         end_time = time.time()
#         print("the total execute time of test1 is %s"%(end_time-start_time))
#     return decorate()
#
#
# @decorator
# def test1():
#     time.sleep(3)
#     print("in the test 1")
#
usernametrue = '123'
passwordreal = '123'

def authouter(authtype):
    print('access type is %s'%authtype)
    def auth(function):
        def decorate(*args, **kwargs):
            if authtype == 'local':
                username = input('please input username').strip()
                password = input('please input password').strip()

                if username == usernametrue and password == passwordreal:
                    print('login success!!')
                    func = function(*args, **kwargs)
                    print('after login')
                    return func
                else:
                    exit('invalid username or password')
            elif authtype == 'ldap':
                print('the authtype is not local')

        return decorate
    return auth


def index():
    print('welcome to index')


@authouter(authtype = 'local')
def home():
    print('welcome to home')
    return 'from home'


@authouter(authtype= 'ldap')
def bbs():
    print('welcome to bbs')

bbs()

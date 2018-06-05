# Author: Real   
# CreateTime 6/4/2018-12:20 PM   
# IDE: PyCharm
# new comment

# 断言assert 被用于在后面比较重要的程序执行之前，检查条件是否符合。断言的作用可以被视为安检
def func():
    print('test function will be execute only if the assert is established')


test_str = 'a string'


assert type(test_str) is int

func()
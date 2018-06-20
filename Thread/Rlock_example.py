# Author: Real   
# CreateTime 6/20/2018-1:57 PM   
# IDE: PyCharm

# RLock 是递归锁，递归锁的出现是为了防止在程序有套索的情况下找不到对应的钥匙而出现锁死的情况
import threading

num1, num2 = 0, 0
locker = threading.RLock()


def func1():
    print('grab the first part of the data')
    locker.acquire()
    global num1
    num1 += 1
    locker.release()
    return num1


def func2():
    print('grab the second part of the data')
    locker.acquire()
    global num2
    num2 += 1
    locker.release()
    return num2


def func3():
    locker.acquire()
    func1()
    print('after func1 and before func2')
    func2()
    locker.release()


for i in range(10):
    t = threading.Thread(target=func3())
    t.start()

while threading.active_count() != 1:
    print(threading.active_count())
else:
    print("all thread has been done")
    print("")

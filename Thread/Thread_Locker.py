# Author: Real   
# CreateTime 6/20/2018-1:22 PM   
# IDE: PyCharm
# 全局解释器锁，是为了让同一时间只有一个线程能修改某一变量
import threading
import time

locker = threading.Lock()

def run(n):
    locker.acquire() #在修改变量之前获取一把锁，把进程上锁。
    global num
    num +=1
    locker.release() #在变量修改完成之后释放锁


num = 0

for i in range(50):
    list = []
    t1 = threading.Thread(target=run,args=(i,))
    # t1.setDaemon(True)   设置守护线程
    t1.start()
    list.append(t1)


for t1 in list:
    t1.join()


print('number is',num)
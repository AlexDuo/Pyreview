# Author: Real   
# CreateTime 6/6/2018-3:45 PM   
# IDE: PyCharm

import threading
import time


def run(n):
    print('thread %s is running'%n)
    time.sleep(2)

start_time = time.time()
for i in range(50):
    list = []
    t1 = threading.Thread(target=run,args=(i,))
    t1.start()
    list.append(t1)

for t1 in list:
    t1.join()

cost = time.time()-start_time
print('all thread has already finished',threading.current_thread()) #程序本身就是主线程，主线程用循环启动了子线程
print(cost)
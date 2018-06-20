# Author: Real   
# CreateTime 6/20/2018-2:09 PM   
# IDE: PyCharm

# 互斥所是为了实现同一个时间只有一个进程在修改数据，而semaphore是同时允许一定数量的线程更改数据，比如餐馆有三个座位，那么只允许有三个客人同时进餐

import threading
import time

semaphore = threading.BoundedSemaphore(5)  # 最多允许有5个线程同时运行


def run(n):
    global num
    semaphore.acquire()
    num += 1
    time.sleep(1)
    print("run the thread %s" % n)
    semaphore.release()


num = 0

for i in range(20):
    t = threading.Thread(target=run, args=(i,))
    t.start()

while threading.active_count() != 1:
    pass
else:
    print("all thread have been done")
    print(num)

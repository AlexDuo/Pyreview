# Author: Real   
# CreateTime 6/20/2018-2:29 PM   
# IDE: PyCharm
import threading
import time

# An event is a simple synchronization(同步) object;
# the event represents an internal flag
# the threads can wait for the flag to be set, or clear the flag themslves

# create an event object
event = threading.Event()

# a client thread can wait for the flag to be set
 # wait是等待标志位，如果标志位被设定了，直接通过，如果标志位没有被设定，那么等待直至设定


# if the flag is set, the wait method doesn't do anything.

# if the flag is cleared, wait will block until it becomes set again.

# any number of threads may wait for the same event

def traffic_light():
    count = 1
    event.set()
    while True:
        if count > 5 and count <=10:
            event.clear()  # 把标志位清楚
            print('\033[41;m 红灯\033[0m')
        elif count > 10:
            event.set()  # 设置标志位
            count = 0
        else:
            print('\033[42;1m 绿灯\033[0m')

        time.sleep(0.5)
        count += 1

def car(name):
    while True:
        if event.is_set(): #如果设置了标志位
            print('%s car is running'%name)
            time.sleep(0.6)
        else:
            print('%s car is waiting'%name)
            event.wait()
            print('green light is on!')




t = threading.Thread(target=traffic_light,)
t.start()

t1 = threading.Thread(target=car,args=('Tesla',))
t1.start()
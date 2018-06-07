# Author: Real   
# CreateTime 6/6/2018-3:21 PM   
# IDE: PyCharm

import threading
import time

def run(n):
    time.sleep(2)
    print('task',n)





t1 = threading.Thread(target=run,args=('t1',))
t1.start()

t2 = threading.Thread(target=run,args=('t2',))
t2.start()

t2 = threading.Thread(target=run,args=('t3',))
t2.start()

t2 = threading.Thread(target=run,args=('t4',))
t2.start()
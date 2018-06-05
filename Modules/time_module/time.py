# Author: Real   
# CreateTime 5/30/2018-10:30 AM   
# IDE: PyCharm

import time
import datetime

# time.time() #1970-now
#
# print(time.time())
#
# print(time.localtime())
# print(time.localtime())
#
# print(time.struct_time)
#
# print(time.gmtime())

x = time.localtime()

# print(help(x))
print(time.asctime()) #接受元组
print(time.ctime()) #接受秒


print(datetime.datetime.now())
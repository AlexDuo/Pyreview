# Author: Real   
# CreateTime 5/30/2018-11:20 AM   
# IDE: PyCharm

import random


# print(random.randint(1,7))
# print(random.randint(1,7))
# print(random.randint(1,7))
# print(random.randint(1,7))
# print(random.randint(1,7))

checkcode = ''


for i in range(4):
    current = random.randint(0,3)
    if i == current:
        letter = chr(random.randint(65,90))
        checkcode += str(letter)
    else:
        checkcode+=str(current)


print(checkcode)
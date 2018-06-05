# Author: Real   
# CreateTime 5/31/2018-9:59 PM   
# IDE: PyCharm


try: #将有可能发生问题的代码放进 try里面
    data = [1]
    print(data[2])

# except IndexError: #可以预先设置错误的类型来抓取固定的错误 也可以采取元组形式抓取多个错误并采取一种解决办法(不推荐)
#
#     print('the key you input is not exist')
except Exception as e: #这种方法是抓取全部错误，只要有错误就抓取，然后在根据系统的提示打印错误类型

    print('There is some mistake but I do not no, the system said "%s"'%e)



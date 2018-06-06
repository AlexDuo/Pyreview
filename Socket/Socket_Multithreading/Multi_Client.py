# Author: Real   
# CreateTime 6/3/2018-1:55 PM   
# IDE: PyCharm

import socket


client = socket.socket() #定义协议类型，括号内传入地址簇.不写的时候默认会传出 IPv4 和 TCP

#因为connect方法只接受一个address 参数所以我们要以元组的形式传入参数
client.connect(('localhost',9999))

# 注意在python3中socket只能发送bytes类型的数据
while True:
    msg = input('Please input the content you want to send to server').strip()
    client.send(msg.encode('utf-8'))
    # 将接受到的数据赋值给data变量，recv函数传入要接受的数据的的最大大小单位是字节
    data = client.recv(51200)
    print(data.decode())

client.close()
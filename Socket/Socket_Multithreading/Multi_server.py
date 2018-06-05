# Author: Real   
# CreateTime 6/3/2018-1:55 PM   
# IDE: PyCharm

import socket

multi_server = socket.socket()

multi_server.bind(('localhost',6969))

multi_server.listen() #listen 后面的参数类型是numeric的，是为了设置最多可以挂起的链接的个数

while True:
    conn,addr = multi_server.accept()

    while True:

        data = conn.recv(51200)

        print('the data we receive from client is %s'%data)

        if not data:
            print('We lost connection with client')

        conn.send(data.upper())


multi_server.close()






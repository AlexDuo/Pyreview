# Author: Real   
# CreateTime 6/5/2018-1:56 PM   
# IDE: PyCharm

# SSH  secure shell 安全外壳协议

# socket 粘包，即两次连续发送数据，会被黏连
import socket, os

server = socket.socket()

server.bind(('localhost',9999))

server.listen()

while True:

    connection, address = server.accept()

    print('the address of new connection is %s',address)

    while True:

        data = connection.recv(1024)

        if not data:
            print('the connection with client has already lost')
            break
        print('execute the command', data)

        cmd_receive = os.popen(data.decode()).read()
        if len(cmd_receive) == 0:
            cmd_receive= 'invalid command line'


        connection.send(str(len(cmd_receive.encode())).encode('utf-8')) #整数是不能encode的字符串能encode

        client_ack = connection.recv(1024) #在两次send之间增加一次交互防止黏连

        connection.send(cmd_receive.encode('utf-8'))

server.close()

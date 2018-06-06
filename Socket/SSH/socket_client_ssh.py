# Author: Real   
# CreateTime 6/5/2018-2:11 PM   
# IDE: PyCharm

import socket

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = input('please input the cmd').strip()

    if len(cmd) == 0: continue

    client.send(cmd.encode('utf-8'))

    cmd_receive_size = client.recv(1024)  # 第一步客户端先接收传入的数据的大小(长度)

    client.send('in case of package stick, and getting ready to send the data'.encode('utf-8'))

    print('the length of the command is', cmd_receive_size)

    received_length = 0
    received_data = b''
    while received_length < int(cmd_receive_size.decode()):
        data = client.recv(1024)
        received_length += len(data)
        # print(data.decode())
        print(received_length)
        received_data += data
    else:
        print('cmd receive job done!')

    # cmd_receive = client.recv(2048)
    #
    # print(cmd_receive.decode())
    print(received_data.decode())

client.close()

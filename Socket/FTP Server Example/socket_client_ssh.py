# Author: Real   
# CreateTime 6/5/2018-2:11 PM   
# IDE: PyCharm

import socket

client = socket.socket()

client.connect(('localhost', 9999))

while True:
    cmd = input('please input the cmd').strip()
    if len(cmd) == 0: continue
    if cmd.startswith('get'):
        client.send(cmd)
        server_response = client.recv(1024)
        print('server response',server_response)
        client.send('getting ready to receive file')
        file_total_size = int(server_response.decode())
        received_size = 0
        filename = cmd.split()[1]
        f = open(filename + 'copied','wb')
        while received_size < file_total_size:
            data = client.recv(1024)
            received_size += len(data)
            f.write(data)
            print(file_total_size,received_size)
        else:
            print('file receive done')
            f.close()





client.close()

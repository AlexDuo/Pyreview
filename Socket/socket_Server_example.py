# Author: Real   
# CreateTime 6/1/2018-12:41 PM   
# IDE: PyCharm

# 这是服务器端


import socket

# 声明协议类型
server = socket.socket()

# 标记要监听的端口，与建立连接一样它也只接受一个参数，可以用元组形式传入
server.bind(('localhost', 6969))

# 进行监听
server.listen()

# 等待通信接入,接入连通后 accept 会返回两个值一个是链接一个是对方的地址
conn, addr = server.accept() #conn 就是客户端请求链接后，服务器端为这个链接请求生成的一个实例

# 将接受到的数据存入data变量中，最大接受量1024字节
data = conn.recv(1024)

# 打印接受到的数据
print('the data we received from client is %s' % data.decode())

# 将接受到的数据以大写的行事反馈给client
conn.send(data.upper())

server.close()

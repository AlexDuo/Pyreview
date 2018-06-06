# Author: Real   
# CreateTime 6/1/2018-12:18 PM   
# IDE: PyCharm

#这是客户端


# 地址簇(位于网络层)也可以理解成 IPv4 或者 IPv6
import socket


# socket.AF_UNIX 与unix进行通信的协议 本机进程之间通信也是用过AF_UNIX(相当于在在本机做了一个local的socket，两个继承通过这个进行通信)
#
# socket.AF_INET IPv4 协议
#
# socket.AF_INET6 IPv6 协议


# 传输层
# socket.SOCK_STREAM 这个是for TCP

# socket.SOCK_DGRAM 这个是 for UDP

# socket.SOCK_RAW 这个是 for 原始套接字 普通的套接字无法处理ICMP\IGMP等网络报文 但是 SOCK_RAW可以

# 这个语句会统摄声明socket协议类型和socket链接对象
client = socket.socket() #定义协议类型，括号内传入地址簇.不写的时候默认会传出 IPv4 和 TCP

#因为connect方法只接受一个address 参数所以我们要以元组的形式传入参数
client.connect(('localhost',9999))

# 注意在python3中socket只能发送bytes类型的数据
client.send('传入中文测试需要encode成ASCII码'.encode("utf-8"))
# 将接受到的数据赋值给data变量，recv函数传入要接受的数据的的最大大小单位是字节
data = client.recv(1024)

print(data.decode())

client.close()
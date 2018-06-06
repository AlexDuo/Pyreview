# Author: Real   
# CreateTime 6/5/2018-5:19 PM   
# IDE: PyCharm

# socket server 最主要的最用就是实现并发处理(官方释义：socketserver module simplfies the task of writing network servers)

# steps to create socketserver:
# # 1. create a request handler class by subclassing the baserequesthandlerclass and overrriding its handel() method
# #   需要自己创建一个请求处理类并且要继承baserequesthandlerclass 并要重写父类中的 handel方法
# # 2. must instantiate on of the server classes,passing it the servers address and the request handler class
# #    你必须实例化server classes 中的一个（例如TCPServer），并且传递Server ip和上面已经创建好的请求处理类给这个TCPServer
# # 3. Then you can call the handle_request() or serve_forever() method of the server object to process one of many requests
# # server.handel_request() 只处理一个请求
# # server.serve_forever() 处理多个请求，并且永远执行
# #
# # 4. finally, call server_close() to close the socket

import socketserver


# 需要自己创建一个请求处理类并且要继承baserequesthandlerclass
class MyTCPHandeler(socketserver.BaseRequestHandler):
    # 并要重写父类中的 handel方法
    def handle(self):#与客户端所有的交互都是在handle中完成的
        while True:
            try:
                self.data = self.request.recv(1024).strip()
                print('{} wrote'.format(self.client_address[0]))
                print(self.data.decode())
                self.request.send(self.data.upper())
            except ConnectionResetError as e:
                print('the error is ',e)
                break



if __name__ == '__main__':
    HOST,PORT = 'localhost',9999
# 你必须实例化server classes 中的一个（例如TCPServer），并且传递Server ip和上面已经创建好的请求处理类给这个TCPServer
server = socketserver.ThreadingTCPServer((HOST,PORT),MyTCPHandeler) #ThreadTCPServer 多线程TCP服务
# server = socketserver.ForkingTCPServer((HOST,PORT),MyTCPHandeler) #forkingTCPServer 是多进程 forking tcp server 在WINDOWS不好用
server.serve_forever()


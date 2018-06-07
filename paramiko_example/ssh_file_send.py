# Author: Real   
# CreateTime 6/6/2018-10:27 AM   
# IDE: PyCharm


import paramiko

if __name__ == '__main__':
    hostname = ''
    hostport = 0
    username = ''
    password = ''

# 以下两条语句仅仅是建立链接通道
transport = paramiko.Transport((hostname, hostport))
transport.connect(username=username, password=password)

# 以下实例定义了文件如何传输和如何交互
sftp = paramiko.SFTPClient.from_transport(transport)

# 将local的文件上传到远程
sftp.put('/local/filename','remote/newfilename')
# 将远程的文件下载到local
sftp.get('remote/filename','local/newfilename')

transport.close()
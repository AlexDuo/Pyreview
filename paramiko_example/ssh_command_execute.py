# Author: Real   
# CreateTime 6/6/2018-9:26 AM   
# IDE: PyCharm

import paramiko

ssh = paramiko.SSHClient()  # SSH就是一个客户端

if __name__ == '__main__':
    hostname = ''
    portnumber = 0
    username = ''
    password = ''

ssh.connect(hostname=hostname, port=portnumber, username=username, password=password)

stdin,stdout,stderr = ssh.exec_command('df') #执行的命令会返回三个结果，标准输入，标准输出，标准错误

result = stdout.read()

error = stderr.read()


ssh.close()
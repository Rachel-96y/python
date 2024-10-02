#TCP服务端程序  _servers.py
#导入socket 库
#等待客户端来连接
from socket import *  #暂时这么写
IP = '192.168.43.229'  #主机地址为 127.0.0.1 
PORT = 50000  #端口号
BUFLEN = 512  #定义一次从socket缓冲区最多读入512字节数据
listen_socket =  socket(AF_INET, SOCK_STREAM)  #实例化一个socket对象
#参数 AF_INET 表示该socket网络使用IP协议
#参数SOCK_STREAM表示该socket传输层使用tcp协议
listen_socket.bind((IP, PORT))  #socket绑定地址和端口
#使socket处于监听状态，等待客户端的连接请求
listen_socket.listen(5)  #参数5表示最多接受多少个客户端的请求
print(f'{PORT}端口已打开')
data_socket, addr = listen_socket.accept()
print(f'接受一个用户的连接:{addr}')
while True:
    #尝试读取对方的消息
    #BUFLEN 指定从接受缓冲里最多读取多少字节
    result = data_socket.recv(BUFLEN)
    if not result:
        break
    info = result.decode()
    print(f'对方的信息是: {info}')
data_socket.close()
listen_socket.close()


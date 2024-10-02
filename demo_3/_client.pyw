#TCP客户端程序 _client.py
from socket import *
IP = '192.168.1.3'  #设置IP地址
SERVER_PORT = 50000  #端口号
BUFLEN = 512 #最大读入的字节流长度
data_socket = socket(AF_INET, SOCK_STREAM)  #实例化对象并指明协议
data_socket.connect((IP, SERVER_PORT))  #连接服务端socket
while True:
    #从终端读入用户输入的字符串
    to_send = input('请输入消息： ')
    if to_send =='exit':
        break
    data_socket.send(to_send.encode())  #发送消息编码为bytes流对象

deta_socket.close()

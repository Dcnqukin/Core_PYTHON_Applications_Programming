#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from socket import *
from time import ctime
HOST=''
PORT = 21567
BUFSIZ = 1024
'''BUFSIZ = 1kB'''
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print('waiting for connection ...')
    tcpCliSock, addr = tcpSerSock.accept()
    '''tcpSerSock.accept()返回两个结果，第一个放入tcpCliSock,第二个放入addr'''
    print('...connected from:', addr)

    while True:
        data = tcpCliSock.recv(BUFSIZ)
        if not data:
            break
        tcpCliSock.send(bytes('[%s] %s' % (ctime(), data.decode('utf-8')), 'utf-8'))

    tcpCliSock.close()

tcpSerSock.close()


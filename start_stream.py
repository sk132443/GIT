
from socket import *
import time

rdd = list()
with open("MobyDick_full.txt", 'r') as ad:
    for line in ad:
        rdd.append(line)

HOST = 'localhost'
PORT = 9998
ADDR = (HOST, PORT)
tcpSock = socket(AF_INET, SOCK_STREAM)
tcpSock.bind(ADDR)
tcpSock.listen(5)


while True:
    c, addr = tcpSock.accept()
    print('got connection')
    for line in rdd:
        try:
            c.send(line.encode())
            time.sleep(1)
        except:
            break
    c.close()
    print('disconnected')

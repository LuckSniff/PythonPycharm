import socket

def printRevData(revData):
    print(revData.decode('utf-8'))


udpServer = socket.socket(type=socket.SOCK_DGRAM)
ipAndPort = ('127.0.0.1',8080)
udpServer.bind(ipAndPort)

while True:
    revData,addr = udpServer.recvfrom(1024)
    printRevData(revData)
    sendData = input('>>>').encode('utf-8')
    udpServer.sendto(sendData,addr)

udpServer.close()
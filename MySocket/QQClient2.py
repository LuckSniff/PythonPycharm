import socket

def printRevData(revData):
    print(revData.decode('utf-8'))


udpClient = socket.socket(type=socket.SOCK_DGRAM)
serverIpAndPort = ('127.0.0.1',8080)

while True:
    sendData = input('>>>').encode('utf-8')
    udpClient.sendto(sendData, serverIpAndPort)
    revData,addr = udpClient.recvfrom(1024)
    printRevData(revData)

udpServer.close()
import struct
import socket

clientSocket = socket.socket()
serverAddr = ('127.0.0.1',8081)
clientSocket.connect(serverAddr)

while True:
    cmd = input('>>>').encode('utf-8')
    clientSocket.sendto(cmd, serverAddr)
    recDataLen = struct.unpack('i', clientSocket.recv(4))[0]
    data = b''
    while True:
        data += clientSocket.recv(1024)
        if( len(data) >= recDataLen ):
            break
    print(data.decode('gbk'))           #注意，接受来自subprocess的数据，是gbk的编码格式

conn.close()
serverSocket.close()

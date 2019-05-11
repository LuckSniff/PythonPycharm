import socket
import struct
import json
from ftp import config

sk = socket.socket()
addr = (config.serverIp, config.serverPort)
sk.bind(addr)
sk.listen()

conn,addr = sk.accept()
headLen = conn.recv(4)
headLen = struct.unpack('i',headLen)[0]
print(headLen)
jsonHead = conn.recv(headLen).decode('utf-8')
head = json.loads(jsonHead)

fileSize = head['fileSize']
everyReadSize = 1024
with open(head['fileName'],'wb') as f:
    while True:
        if fileSize >= everyReadSize:
            content = conn.recv(everyReadSize)
            f.write(content)
            fileSize -= everyReadSize
        else:
            content = conn.recv(fileSize)
            f.write(content)
            break
conn.close()
sk.close()
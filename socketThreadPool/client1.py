import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8081))

ret = sk.recv(1024).decode('utf-8')
print(ret)
sendData = input('>>>').encode('utf-8')
sk.send(sendData)

sk.close()
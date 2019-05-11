import socket

sk = socket.socket()
sk.connect(('127.0.0.1',8081))

sk.send('Li'.encode('utf-8'))
recData = sk.recv(1024).decode('utf-8')
print(recData)

sendData = input('>>>').encode('utf-8')
sk.send(sendData)

sk.close()

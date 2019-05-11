import socket

sk = socket.socket()

sk.connect(('127.0.0.1',8081))

data = input(">>>").encode('utf-8')
sk.send(data)

data = input(">>>").encode('utf-8')


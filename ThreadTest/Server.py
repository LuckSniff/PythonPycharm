import  socket

sk = socket.socket()
sk.bind(('127.0.0.1',8081))
sk.listen()

conn,addr = sk.accept()
conn.send('你好'.encode('utf-8'))

msg = conn.recv(1024).decode('utf-8')
print(msg)
ret = input('>>>')
conn.send(ret.encode('utf-8'))

conn.close()
sk.close()
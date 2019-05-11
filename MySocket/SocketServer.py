import socket

socketObj = socket.socket()
socketObj.bind(('127.0.0.1',8089))
socketObj.listen()
print('begin listen port')

while True:
    conn, addr = socketObj.accept()
    print('has people come from client  addr is', addr)
    while True:
        receiveData = conn.recv(1024).decode('utf-8')
        print(receiveData)
        if ( 'bye' in receiveData ):
            conn.send(b'bye')
            break
        msg = input('>>>')
        conn.send(bytes(msg, encoding='utf-8'))
    conn.close()

socketObj.close()
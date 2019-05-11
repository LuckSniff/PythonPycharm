import socket

socketObj = socket.socket()
socketObj.connect(('127.0.0.1',8089))

while True:
    sendData = input('>>>')
    socketObj.send(bytes('client2： '+sendData,encoding='utf-8'))
    recData = socketObj.recv(1024)
    print(recData.decode('utf-8'))
    if('bye' in sendData):
        break

socketObj.close()
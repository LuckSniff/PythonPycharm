import selectors
import socket

sel = selectors.DefaultSelector()

def accept(socket,mask):
    conn,addr = socket.accept()
    conn.setblocking(False)
    sel.register(conn,selectors.EVENT_READ,read)

def read(conn,mask):
    data = conn.recv(1000)
    if data:
        conn.send(data)
    else:
        sel.unregister(conn)
        conn.close()

sk = socket.socket()
sk.bind(('127.0.0.1',8081))
sk.listen()
sk.setblocking(False)

sel.register(sk,selectors.EVENT_READ,accept)

while True:
    events = sel.select()
    for key,mask in events:
        print(key)          #key is class called SelectorKey
        print(mask)         # 1
        callback = key.data
        print(callback)
        callback(key.fileobj,mask)

print('ends')

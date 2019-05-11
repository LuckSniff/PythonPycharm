import socket
from multiprocessing import Pool

def dealConn(conn,addr):
    conn.send(b'hello')
    print(conn.recv(1024).decode('utf-8'))
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 8081))
    sk.listen()

    threadPool = Pool(5)

    while True:
        conn, addr = sk.accept()
        print(addr)
        threadPool.apply_async(func=dealConn, args=(conn,addr))

    sk.close()
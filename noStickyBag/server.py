import struct
import socket
import subprocess

serverSocket = socket.socket()
serverAddr = ('127.0.0.1', 8081)
serverSocket.bind(serverAddr)
serverSocket.listen()

while True:
    conn, addr = serverSocket.accept()
    print('client from ', addr)
    while True:
        cmd = conn.recv(1024)
        if not cmd: break
        res = subprocess.Popen(cmd.decode('utf-8'),
                               shell=True,
                               stdin=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               stdout=subprocess.PIPE)
        err = res.stderr.read()
        if err:
            ret = err
        else:
            ret = res.stdout.read()
        conn.send(struct.pack('i', len(ret)))
        conn.send(ret)
    conn.close()

serverSocket.close()
import socket

def createUDPServerSocket(addr):
    sk = socket.socket(socket.SOCK_DGRAM)
    sk.bind(addr)
    return sk

def createUDPClientSocket():
    sk = socket.socket(socket.SOCK_DGRAM)
    return sk




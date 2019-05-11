import socket
import struct
import logging
from ftp import  config
from ftp import factorySocket
from ftp import FactoryLogging
import hashlib
import json

#如何实现多用户同时登陆?

def recHeadData(conn):
    headLen = conn.recv(4)
    headLen = struct.unpack('i', headLen)[0]
    jsonHead = conn.recv(headLen).decode('utf-8')
    head = json.loads(jsonHead)
    return head

logger = FactoryLogging.factoryLogging().getLogging()


addr = (config.serverIp,config.serverPort)
sk = factorySocket.createUDPServerSocket(addr)


while True:
    conn,addr = serverSocket.recv(1024)
    logger.debug('client ',addr,' connect')






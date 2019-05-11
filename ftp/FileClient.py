import socket
import struct
import json
import os
from ftp import config

def getFileSize(filePath):
    return os.path.getsize(filePath)

def getRemoteConnectedObj(addr):
    sk = socket.socket()
    sk.connect(addr)
    return sk

def getJsonByteHead(head):
    jsonHead = json.dumps(head)
    byteJsonHead = jsonHead.encode('utf-8')  # 字符串转byte
    return  byteJsonHead

def getJsonByteHeadPackLen(jsonByteHead):
    headLen = len(jsonByteHead)
    packHeadLen = struct.pack('i', headLen)
    return packHeadLen

head = {'fileName': None,'filePath': None, 'fileSize':None}
head['filePath'] = r'E:\movie.mp4'
head['fileName'] = 'movie.mp4'
head['fileSize'] = getFileSize(head['filePath'])

addr = (config.serverIp, config.serverPort)
sk = getRemoteConnectedObj(addr)

byteJsonHead = getJsonByteHead(head)
byteJsonHeadPackLen = getJsonByteHeadPackLen(byteJsonHead)
sk.send(byteJsonHeadPackLen)
sk.send(byteJsonHead)

# 需要注意的是，每次读取文件大小的4096，当最后一次读取时，文件大小小于4096，就按照剩下的读取
fileSize = head['fileSize']
everyReadSize = 1024
with open(head['filePath'],'rb') as f:
    while True:
        if fileSize >= everyReadSize:
            content = f.read(everyReadSize)
            sk.send(content)
            fileSize -= everyReadSize
        else:
            content = f.read(fileSize)
            sk.send(content)
            break

sk.close()


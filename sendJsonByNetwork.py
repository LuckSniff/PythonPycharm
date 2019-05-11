import json
import urllib.request

def sendVoiceToServer(url,sendData):
    sendData = sendData.encode('utf-8')
    request = urllib.request.Request(url=url, data=sendData)
    response = urllib.request.urlopen(request)

if __name__ == '__main__':
    url = 'http://172.20.43.178:8080/zzaf/voice'
    sendData = '哇呀呀！！！ 吾命休矣....救命'
    sendVoiceToServer(url, sendData)
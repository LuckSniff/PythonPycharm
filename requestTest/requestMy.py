import requests
from multiprocessing import Pool
import time

def getContent(url):
    reponse = requests.get(url)
    if reponse.status_code == 200:
        return url,reponse.content.decode('utf-8')

def printInfo(args):
    url,content = args
    print(url,len(content))

if __name__ == '__main__':
    start = time.time()
    threadPool = Pool(5)
    urls = ["https://www.bilibili.com/","https://www.baidu.com","http://muchong.com/","https://www.cqu.edu.cn/"]
    for url in urls:
        threadPool.apply_async(func=getContent,args=(url,),callback=printInfo)
    threadPool.close()
    threadPool.join()
    end = time.time()
    print('time : ',str(end-start))

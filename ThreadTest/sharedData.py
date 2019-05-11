from multiprocessing import Manager,Process,Lock

def main(dic,lock):
    lock.acquire()
    dic['count'] -= 1
    lock.release()

if __name__ == '__main__':
    lock = Lock()
    proList = []
    manager = Manager()
    syncDict = manager.dict({'count':100})      #创建一个数据共享的字典
    for i in range(50):
        p = Process(target=main,args=(syncDict,lock))
        proList.append(p)
        p.start()
    for p in proList: p.join()
    print(syncDict)


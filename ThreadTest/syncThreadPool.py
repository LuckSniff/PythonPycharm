from multiprocessing import Pool
import time
import os

def func(n):
    print('start %s'%n,os.getpid())
    time.sleep(1)
    print('end %s' % n, os.getpid())
    return n*n

if __name__ == '__main__':
    p = Pool(5)
    for i in range(10):
        res = p.apply_async(func,args=(i,))
        print(res.get())
    p.close()       #进程池不在接受任务
    p.join()        #感知进程池中的任务执行结束
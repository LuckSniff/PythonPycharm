from  multiprocessing  import  Process
import os

def func():
    global n
    n = 0
    print('pid %s'%os.getpid(),n)

if __name__ == '__main__':
    global n
    n = 100
    p = Process(target=func)
    p.start()
    p.join()
    print(os.getpid(),n)

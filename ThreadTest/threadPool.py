from multiprocessing import Pool

def func(n):
    print(n)
    return n*n

if __name__ == '__main__':
    threadPool = Pool(5)             #进程池中的进程数（大都是CPU核数+1）
    ret = threadPool.map(func,[(1),(3)])    #第二个参数，必须是可迭代对象，且每个迭代就是传入的参数
    #这样写就会执行进程完成任务
    print(ret)
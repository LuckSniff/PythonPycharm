from multiprocessing import Pool

def func1(n,i):
    print('func 1 %s'%i)
    return n*n

def func2(nn):
    print('func2 %s'%nn)
    return nn

if __name__ == '__main__':
    pool = Pool(5)
    for i in range(10):
        pool.apply_async(func=func1,args=(1,i),callback=func2)
    pool.close()
    pool.join()
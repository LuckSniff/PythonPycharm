import time
'''
def colRunningTime_wrapper(func):
    def inner(*arg,**args):
        start = time.time()
        ret = func(*arg,**args)
        end = time.time()
        print('time : '+str(end-start))
        return ret
    return inner


def colMovingAverageInit(func):
    def inner(*arg,**args):
        g = func(*arg,**args)
        g.__next__()
        return g
    return inner


@colMovingAverageInit
def colMovingAverage():
    sum = 0
    count = 0
    avg = 0
    while True:
        num = yield avg
        sum += num
        count += 1
        avg = sum / count

g = colMovingAverage()
ret = g.send(1)
ret = g.send(2)
print(ret)
'''

def recordRunningTime(func):
    def inner(*args, **kwargs):
        start = time.time()
        ret = func(*args, **kwargs)
        end = time.time()
        print(end-start)
        return ret
    return inner

@recordRunningTime
def func(a):
    print(a)
    time.sleep(1)

a = func('ok')
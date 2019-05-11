import time

def printProcessBar():
    for i in range(0,101,2):
        time.sleep(0.1)
        per_str = '\r%s%% : %s' %(i,'*' * i) if not i==100 else 'end'
        print(per_str,end=' ',flush=True)



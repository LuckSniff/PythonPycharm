from multiprocessing import Process,Event
import time
import random

def car(i,event):
    if not event.is_set():
        print(i,' 等待通行')
        event.wait()
    print(i,' 通过')

def light(event):
    while True:
        print('\033[31m红灯亮\033[0m')
        event.clear()
        time.sleep(2)

        print('\033[30m绿灯亮\033[0m')
        event.set()
        time.sleep(2)


if __name__ == '__main__':
    event = Event()
    traffic = Process(target=light,args=(event,))
    traffic.start()

    for i in range(10):
        carProcess = Process(target=car, args=(i,event,))
        carProcess.start()
        time.sleep(random.random())

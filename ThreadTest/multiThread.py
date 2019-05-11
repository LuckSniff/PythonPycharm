from multiprocessing import Process
import time
import os

class myProcess(Process):
    def __init__(self,arg1):
        super().__init__()
        self.arg1 = arg1

    def run(self):
        print(os.getpid())
        print(self.arg1)


if __name__ == '__main__':
    p1 = myProcess(1)
    p1.start()



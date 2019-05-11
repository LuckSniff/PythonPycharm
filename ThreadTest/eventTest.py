from multiprocessing import  Process
from multiprocessing import  Event

'''
from multiprocessing import  Event
e = Event() #创建事件
e.is_set()  #查看事件是否阻塞  False阻塞  True非阻塞
e.set()     #设置为非阻塞
e.clear()   #将事件设置为阻塞
e.wait()    #根据当前e的值，决定运行这句话的时候是否阻塞，当有用户调用e.set()后，e.wait()不在阻塞
'''

e = Event()
print(e.is_set())           #查看一个事件的状态，默认是阻塞的--False
print(123)
e.wait()                    #根据is_set()的值，决定是否阻塞，当is_set是阻塞的时候，该处就阻塞，若不是，就不阻塞
print(12345)


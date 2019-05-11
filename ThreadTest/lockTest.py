from multiprocessing import  Process
import json
import time
from multiprocessing import Lock

def updateTicketNum(newTicketNum):
    time.sleep(0.1)
    with open('ticket','w') as f:
        json.dump({'ticket':newTicketNum},f)

def queyRemainingTicket():
    with open('ticket', 'r') as f:
        ticketData = json.load(f)
        time.sleep(0.1)
    return ticketData['ticket']

def buyTicket(i,lock):
    lock.acquire()
    remaingTicket = queyRemainingTicket()
    if remaingTicket > 0:
        print(i,'buy one ticket')
        updateTicketNum(remaingTicket-1)
    else:
        print(i,'no ticket')
    lock.release()


if __name__ == '__main__':
    lock = Lock()
    for i in range(10):
        p = Process(target=buyTicket,args=(i,lock))
        p.start()
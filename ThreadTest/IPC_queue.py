from multiprocessing import Queue

q = Queue(5)
q.put(1)
q.get()
try:
    q.get_nowait()
except Exception:
    print('队列为空')

print('end')



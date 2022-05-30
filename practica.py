
from queue import Queue # Python 3.x
from threading import Thread

def foo(bar):

    print('hello {0}'.format(bar))   # Python 3.x
    return 'foo'


que = Queue()           # Python 3.x

threads_list = list()

t = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, 'world!'))
t.start()
threads_list.append(t)

t2 = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, 'abastecimientpp'))
t2.start()
threads_list.append(t2)
t3 = Thread(target=lambda q, arg1: q.put(foo(arg1)), args=(que, 'ahsbkask'))
t3.start()
threads_list.append(t3)

# Join all the threads
for t in threads_list:
    t.join()

# Check thread's return value
while not que.empty():
    result = que.get()

    print(result)  
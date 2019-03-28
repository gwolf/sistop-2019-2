from threading import Semaphore

items =['A','B', 'C','D']

for index, item in enumerate(items):   # default is zero
    print(index, item)
mutex_guias = [Semaphore(1) for i in range(5)]

print(len(mutex_guias))

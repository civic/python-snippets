import threading
import time

n = 0
lock = threading.Lock()

def worker():
    global n
    for _ in range(100000):
        lock.acquire()
        n += 1
        lock.release()


th1 = threading.Thread(target=worker, name="a")
th2 = threading.Thread(target=worker, name="b")

th1.start()
th2.start()

th1.join()
th2.join()

print(n)

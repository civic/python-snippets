import threading
import time



def worker():
    for n in range(10):
        print("{}: {}".format(threading.current_thread().name, n))
        time.sleep(0.5)


th1 = threading.Thread(target=worker, name="a")
th2 = threading.Thread(target=worker, name="b")

th1.start()
time.sleep(0.1)
th2.start()

th1.join()
th2.join()


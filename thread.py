import threading


def worker(key):
    for n in range(10):
        print(key, n)


th1 = threading.Thread(target=worker, args="a")
th2 = threading.Thread(target=worker, args="b")

th1.start()
th2.start()

th1.join()
th2.join()


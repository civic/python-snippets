import multiprocessing
import time


def worker(interval):
    for n in range(3):
        time.sleep(interval)
        print("%s --> %d" % (multiprocessing.current_process().name, n))

p1 = multiprocessing.Process(name="a", target=worker, args=(1, ))
p2 = multiprocessing.Process(name="b", target=worker, args=(2, ))

p1.start()
p2.start()

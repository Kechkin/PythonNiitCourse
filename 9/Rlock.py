import time
from threading import Thread, RLock


class Base:
    x = 0
    y = 0


def test(n):
    n.acquire()
    i = 2
    while i > 0:
        print("Поток 1!")
        x = input("1x")
        y = input("1y")
        print(f"1 поток {x}{y}")
        i -= 1
    n.release()
    time.sleep(1)


if __name__ == '__main__':
    lock = RLock()
    thr = Thread(target=test, args=(lock,))
    thr.start()
    lock.acquire()
    i = 2
    while i > 0:
        print("Поток 2!")
        x = input("2x")
        y = input("2y")
        print(f"2 поток {x}{y}")
        i -= 1
    lock.release()
    thr.join()

import math
import time
from multiprocessing import Process
from threading import Thread


def find_primes(end, start=3):
    lst = []
    for i in range(start, end + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    print(len(lst))
    return lst


# для последоательного выполнения ~  12
begin = time.perf_counter()
find_primes(10000, 3)
find_primes(20000, 10001)
find_primes(30000, 20001)
print(f"main time: {time.perf_counter() - begin}")


# # для потоков ~ 11
begin = time.perf_counter()
thr1 = Thread(target=find_primes, args=(10000, 3))
thr2 = Thread(target=find_primes, args=(20000, 10000))
thr3 = Thread(target=find_primes, args=(30000, 20000))

thr1.start()
thr2.start()
thr3.start()

thr1.join()
thr2.join()
thr3.join()
print(f"main time: {time.perf_counter() - begin}")

# # для Процесссов ~ 8
if __name__ == '__main__':
    begin = time.perf_counter()
    thr1 = Process(target=find_primes, args=(10000, 3))
    thr2 = Process(target=find_primes, args=(20000, 10001))
    thr3 = Process(target=find_primes, args=(30000, 20001))

    thr1.start()
    thr2.start()
    thr3.start()

    thr1.join()
    thr2.join()
    thr3.join()
    print(f"main time: {time.perf_counter() - begin}")

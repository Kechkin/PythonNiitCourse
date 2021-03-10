import random
import time
import threading


def compute(number):
    print(f"start {number}")
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print(f"end of № {number} затрачено {sleeping}")


start = time.perf_counter()

arr = []

for i in range(5):
    thr = threading.Thread(target=compute, args=(i,))
    thr.start()
    arr.append(thr)

for i in arr:
    i.join()
print("main time:", time.perf_counter() - start)

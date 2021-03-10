import threading
import time
import random

def compute(number):
    a = random.randint(1,5)
    print("start:", number)
    time.sleep(a)
    return "done"

start = time.perf_counter()
    
treads = []
    
for i in range(5):
    thr = threading.Thread(target = compute, args=(i,)) # объект потока
    thr.start() #запуск потока
    treads.append(thr)

for i in treads:
    thr.join() #объединение потоков, ждём пока все завершатся
print(f"main time: {time.perf_counter() - start}")
    


    
    
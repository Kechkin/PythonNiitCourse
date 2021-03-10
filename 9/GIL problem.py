# if __name__ == '__main__':
import threading 
import time

def count(n):
	while n > 0:
		n-=1

c = 80000000
start = time.perf_counter()
t1 = threading.Thread(target=count, args=(c,))
t2 = threading.Thread(target=count, args=(c,))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"time: {time.perf_counter() - start}")

# не дают преимущества из-за GIL
# вместо всех блокировок исп. только один глобальный 
# только один поток может использовать блокировку GIL
# потоки нужны для конкурентности
'''green threads:'''
#выполняются в рамках одного обычного потока, но работается будто с несколькими потоками
#позв. обеспечить конкурентность, без необходимодисти затрачивать время на созд. отдель потоков
# не исполь. процессор
import gevent
import time
import threading

def count(n):
	while n > 0:
		n-=1

c=80000000

start= time.perf_counter()
g1 = gevent.spawn(count, c) #запуск 
g2 = gevent.spawn(count, c) #запуск без ожид. завершение предыдушего
gevent.joinall([g1,g2])
print(f"time: {time.perf_counter() - start}")
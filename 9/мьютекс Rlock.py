from threading import Thread, RLock
import time
import random

class Base:
	x = 0
	y = 0 

def test(lock):
	i = 0
	while i < 2:
		lock.acquire() #блокировка
		Base.x = input("поток 1: x: ")
		Base.y = input("поток 1: y: ")
		print("поток 1 общий:", Base.x, Base.y)
		lock.release() #разблокировка
		i+=1
		time.sleep(1)



if __name__ == '__main__':
	lock = RLock()
	t = Thread(target=test, args=(lock,))
	i = 0
	while i < 2:
		lock.acquire()
		Base.x = input("поток 2 x: ")
		Base.y = input("поток 2 y")
		print("поток 2 общий:", Base.x, Base.y)
		lock.release()
		i+=1
		time.sleep(1)
		t.start()
t.join()

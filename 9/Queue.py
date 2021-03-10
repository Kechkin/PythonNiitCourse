
import multiprocessing
import time



def count(q):
	q.put("from client")
	print(q.get())

c = 80000000

if __name__ == '__main__':
	q = multiprocessing.Queue()
	t1 = multiprocessing.Process(target=count, args=(q,))
	t1.start()
	q.put("from server: hello")
	print(q.get())
	t1.join()

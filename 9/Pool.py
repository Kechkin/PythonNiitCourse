from multiprocessing import Pool
import os
import time

lst = []

def cube(x):
	lst.append(x)
	print(f"This process {os.getpid()} processed values {lst}")
	time.sleep(2)
	return x**2

if __name__ == '__main__':
	pool = Pool(processes=5)  #сколько ядер (логических), столько processes ставить
	res = pool.map(cube, range(1,17))
	print(res)
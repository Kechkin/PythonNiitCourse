from threading import Thread, Condition


arr = []

def test(cv):
	global arr
	with cv:
		while 'exit' not in arr:
			cv.wait()
			print("no 'exit' yet")
	print("exit in arr")
	arr.remove('exit')
	#your code here
	print(f"len arr: {len(arr)}, : {arr}")

if __name__ == '__main__':
	cv = Condition()
	thr = Thread(target=test, args=(cv,))
	thr.start()

	while "exit" not in arr:
		arr.append(input("type text: "))
		with cv:
			cv.notify()
	thr.join()


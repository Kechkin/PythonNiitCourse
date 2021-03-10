import time
class Test():
	def __init__(self):
		self.start = time.time()
	def __enter__(self):
		print("Start")
	def __exit__(self, exc_type, exc_val, exc_tb):
		print(f"finish: {time.time() - self.start}")

with Test():
	for i in range(10):
		time.sleep(1)
		print(i)

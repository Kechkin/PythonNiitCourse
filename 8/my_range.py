class myrange:
	def __init__(self, start , stop, step = 1):
			self.start = start 
			self.stop = stop
			self.step = step
	def __iter__(self):
		return self
	def __next__(self):
		if self.start <= self.stop:
			result, step =  self.start, self.step
			self.start+=step 
			return result
		else:
			raise StopIteration

for i in myrange(1,10, 2):
	print(i)
#реализация функтора

class Test:
	def __init__(self):
		self.count = 0

	def __call__(self, *args, **kwargs):
		print("call")
		self.count +=1
		print(self.count)
		return self.count
c1 = Test()
c1() #count = 1
c1() #count = 2


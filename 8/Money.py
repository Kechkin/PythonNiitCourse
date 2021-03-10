import math

class Money:
	def __init__(self, rub):
		self._rub = rub
		self._dollar = 0
	
	def to_dollar(self, dollar_now):
		self._dollar = math.floor(self._rub / dollar_now)
		self._rub = 0


	def getDollar(self):
		return self._dollar

	def __add__(self, other):
		if isinstance(other, int):
			return self._rub + other

	def __sub__(self, other):
		if isinstance(other, int):
			if self._rub > other:
				return self._rub - other 
			else:
				self._rub = 0
				return self._rub

	def __truediv__(self, other):
		if isinstance(other, int):
			return self._rub // other
			
	def __eq__(self, other):
		return self._rub == other._rub 
	
	def __lt__(self, other):
		return self._rub < other._rub 
	
	def __gt__(self, other):
		return self._rub > other._rub 

u1 = Money(1000)
u2 = Money(100)
u1.to_dollar(70)
print(u1.getDollar())





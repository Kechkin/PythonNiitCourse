class User:
	def __init__(self, name, age):
		self.name = name
		self.age  = age

	def setName(self, setname):
		self.name = setname
	
	def getName(self):
		return self.name
	
	def setAge(self, setage):
		self.age = setage
	
	def getAge(self):
		return self.age

class Worker(User):
	def __init__(self,name,age, salary):
		super().__init__(name, age)
		self.salary = salary
	
	def setSalary(self, setsal):
		self.salary = setsal

	def getSalary(self):
		return self.salary

	def __add__(self, other):
		res = self.salary + other.salary
		return res


user1 = Worker("John", 25, 1000)
user2 = Worker("Jack", 26, 2000)
print(f"Main salary:",user1.salary + user2.salary)
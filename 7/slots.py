class Human:
	__slots__ = "age", "salary", "name" # ограничиеват только этим атрибутами
	def __init__(self, name ,age):
		self.name = name
		self.age = age
		self.salary = 15000

person = Human("alex", 30)
person.age = 31
person.zz = 22 # не даст создать новый атриубут
print(person.age)
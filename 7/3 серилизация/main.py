import pickle

class Human:
	name = "Alex"
	lastname = "Bold"
	age = 34
	city = "LA"
	salary = 5000


m = Human()


with open("Human.data", "wb") as f:
	pickle.dump(m, f)

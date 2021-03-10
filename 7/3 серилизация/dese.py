import pickle
from main import Human

with open("Human.data", "rb") as f:
	m = pickle.load(f)

print(m.name)
print(m.lastname)
print(m.age)
print(m.city)
print(m.salary)
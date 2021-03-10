import time
import random

class Man:
	def __init__(self, name):
		self.name = name

	def solve_task(self):
		print("Not ready yet")


class Pupil(Man):
	def __init__(self, name):
		super().__init__(name)

	def solve_task(self):
		time.sleep(random.randint(3,5))
		print("Not ready yet")

p = Pupil("max")
p.solve_task()
text = "some text \tand tab \tand this"


class IterText:
	def __init__(self, text):
		self.text = text.split("\t")
		print(self.text)
		self.i = 0
	def __iter__(self):
		return self
	def __next__(self):
		if self.i < len(self.text):
			line = self.text[self.i]
			self.i +=1
			return line
		else:
			raise StopIteration


for i in IterText(text):
	print(i)

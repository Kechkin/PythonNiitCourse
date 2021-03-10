import tempfile 
import os

class WrapStrToFile:
	def __init__(self):
		self.filepath = tempfile.mktemp("tmp.txt")
		self._content = None

	@property
	def content(self):
		try:
			f = open(self.filepath, "r")
			for i in f:
				return i
		except Exception as e:
			print("File is not exist")

	@content.setter
	def content(self, value):
		try:
			f = open(self.filepath, "w")
			f.write(value)
		except Exception as e:
			print(f"Error: {e}")

	
	@content.deleter
	def content(self):
		os.remove(self.filepath)
		print("deleted")

p = WrapStrToFile()
p.content
p.content = "test str"
print(p.content)
p.content = "new str"
print(p.content)
del p.content
p.content



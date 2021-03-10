def test(text):
	try:
		with open(text, "r") as f:
			a = [i for i in f]
			for i in a:
				print(i)
				if "\n" in i:
					yield i

	except Exception as e:
		print(f"Error{e}")
text = "file.txt"
f = test(text )
next(f)
next(f)


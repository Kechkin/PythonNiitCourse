
def copyfile(source, destination):
	rfile = ""
	try:
		with open(source, "r") as f:
			rfile = f.read()
	except Exception as e:
		print(f"Error: {e}")

	try:
		with open(destination, "w") as fp:
			fp.write(rfile)
			return "file is ready"
	except Exception as e:
		print(f"Error: {e}")
print(copyfile("source.txt", "destination.txt"))


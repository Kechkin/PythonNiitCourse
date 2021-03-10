def to_title(str):
	arr = str.split(" ")
	for i in range(len(arr)):
		arr[i] = arr[i][0].upper() + arr[i][1:]
	return " ".join(arr)

print(to_title("one two three"))
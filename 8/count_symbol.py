def count_symbol(str, symb):
	arr = str.split(" ")
	count = 0
	for i in range(len(arr)):
		if symb in arr[i]:
			count+=1
	return count
print(count_symbol("Hi Elvis, I am here", "i"))
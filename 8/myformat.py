import re

def myformat(s, *args):
	my_str = re.sub("[\{\}]","",s)
	args_arr = {}

	for i in range(len(args)):
		args_arr[i] = args[i]

	for k,v in args_arr.items():
		if str(k) in my_str:
			my_str = my_str.replace(str(k),str(v))
	return my_str
	
print(myformat("Helloy my {0}, this is a {2} for {1}","friend","you","text"))
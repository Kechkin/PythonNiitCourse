import itertools

def task1(*arr):
	return [i for i in itertools.chain(*arr)]

print(task1([1,2,3],[4,5],[6,7]))



def task2(arr):
	return [i for i in itertools.filterfalse(lambda x: len(x) < 5, arr)]

print(task2(["hello","i","write","cool","code","aaaaa"]))

def task3(s):
	return set([i for i, c in itertools.combinations_with_replacement(s, len(s))])

print(task3("password"))
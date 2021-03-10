#декоратор с подсчетом вызовов функции

count = 0

def wrapper(func):
    def inner(*args):
        res = func(*args)
        global count
        count+=1
        print("count:", count)
        return res
    return inner

@wrapper
def test(a,b):
    return a + b

print(test(10, 20))
print(test(11, 20))
print(test(55, 11))
print(test(77, 21))
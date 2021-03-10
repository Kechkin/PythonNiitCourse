def wrapper(func):
    def inner(*args):
        res = func(*args)
        h = hash(res)
        return h
    return inner

@wrapper
def test(a):
    return a
    
print( test("5W44gsaAwfr"))

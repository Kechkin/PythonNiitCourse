x = 5

def factorial(x):
    if x == 0:
        return 1
    return x * factorial(x - 1)
    
print(factorial(x))

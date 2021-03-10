import random
import string

def make_password(length, flag_upper, flag_lower, flag_digit):
    result =  ""
    for i in range(10000):
        if len(result) == length:
            break
        rand = random.randint(1,3)
            
        if rand == 3 and flag_digit:
            digit = str(random.randint(0,9))
            if not digit in result:
                result+=digit
                    
        elif rand == 2 and flag_lower:
            lower = random.choice(string.ascii_lowercase)
            if not lower in result:
                result+=lower
                
        elif rand == 1 and flag_upper:
            upper = random.choice(string.ascii_uppercase)
            if not upper in result:
                result+=upper
    return result
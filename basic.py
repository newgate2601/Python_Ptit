s = 'Hello World!'

print(s)        # Hello World!
print( s[2:5])  # llo


import math


def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1    

def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)    
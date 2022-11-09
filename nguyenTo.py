import math

def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

test = int( input() )

while( test > 0 ):
    test -= 1

    n = int( input() )

    tong = 0

    for i in range(1, n):
        if(math.gcd(i,n)==1):
            tong+=1

    if(nto(tong) == True ):print("YES")
    else: print("NO")
        



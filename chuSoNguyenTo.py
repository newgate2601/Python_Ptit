import math

def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

test = int( input() )

while(test > 0):
    test -= 1

    s = str( input() )
    
    dai = len(s)

    if( nto(dai) == False ): print("NO")
    else:
        demNT = 0

        for x in s:
            x = int(x)
            if(nto(x) == True):
                demNT+=1
            if( dai - demNT < demNT  ):
                break

        if(dai - demNT < demNT):print("YES")
        else: print("NO")     
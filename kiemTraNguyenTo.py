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
    
    tong = int ( s[len(s)-1] ) + 10*int ( s[len(s)-2] ) + 100*int ( s[len(s)-3] ) + 1000*int ( s[len(s)-4] )
    

    if( nto(tong) == True ): print("YES")
    else: print("NO")
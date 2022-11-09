
import math


def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1            

test = int(input())

while(test>0):
    test-=1

    n = int(input())

    dem = 0

    for i in range(2, n ):
        if(i+6>=n):
            break
        
        if( (snt(i)==1 and snt(i+4)==1 and snt(i+6)==1) or (snt(i)==1 and snt(i+2)==1 and snt(i+6)==1) ):
            dem+=1

    print(dem)

    

                 
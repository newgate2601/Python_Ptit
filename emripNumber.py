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

    xau = ""

    for i in range (2, n ):

        s = str(i)
        q = s[::-1]
        q = int(q)

        if(s!=str(q) and q < n and i < q):
            if(snt(i) == 1 and snt( int(q))==1):
                xau += str(i) + " " + str(q) + " "

    print(xau)            
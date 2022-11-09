


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

    s = str(input())

    a = s.split()

    b = [0]*1000001

    for i in range(0, len(a)):
        a[i] = int( a[i] )

    for i in range(0,len(a)):
        c = a[i]
        while(c>0):
            b[i] += int(c%10)
            c = c/10

    for i in range(0, len(a) - 1):
        for j in  range(i+1, len(a)):
            if(b[i]>b[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t

                w = b[i]
                b[i] = b[j]
                b[j] = w

    for i in range(0, len(a) - 1):
        for j in  range(i+1, len(a)):
            if(b[i]==b[j] and a[i]>a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t  

    oput = ""

    for i in range(0, len(a)):
        oput += str(a[i]) + " "

    print(oput)                     






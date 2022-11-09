


import math

def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1 

n = int(input())

s = str(input())

a = s.split()

b = [0]*1000001

for i in range(0, len(a)):
    a[i] = int( a[i] )
    b[a[i]]+=1

for i in range(0, len(a)):
    if( snt(a[i]) == 1 and b[a[i]]!=0):
        q = ""
        q += str(a[i])+" "+str(b[a[i]])    
        b[a[i]] = 0
        print (q)







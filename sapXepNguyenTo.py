import math
from operator import le


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

list = s.split()

for i in range(0, len(list)):
    list[i] = int( list[i] )

for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if( snt(list[i]) != 1 ):
            break

        if(snt(list[j]) == 1 and list[i] > list[j] ):
            t = list[i]
            list[i] = list[j]
            list[j] = t

q = ""

for i in range(0,len(list)):
    q+=str(list[i])+" "

print(q)    
import math


def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1    

s = str(input())

n,m = s.split()

n = int(n)
m = int(m)

list = []

for i in range(0,n):
    new = []

    ip = str(input())

    a = ip.split()

    for z in range(0, len(a)):
        a[z] = int(a[z]) 
        new.append(a[z])

    list.append(new)    
        

for i in range(0,n):
    q = ""
    for j in range(0,m):

        if( snt(list[i][j]) == 1 ):
            list[i][j] = 1
        else:
            list[i][j] = 0


        q+= str(list[i][j])+" "

    print(q)    

        
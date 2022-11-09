import math


def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1   

list = [1]*99999

z = 2
i = 0

for z in range (0,99999):
    if(snt(z)==1):
        list[i] = z
        i+=1
    else:
        z+=1    

s = str(input())

n, x = s.split()

n = int(n)
x= int(x)

bdau = -1

oput = str(x) +" "

for i in range(0, n):
    x += list[i]
    oput += str(x) + " "

print(oput)    

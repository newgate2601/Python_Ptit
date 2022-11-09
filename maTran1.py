import math


def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1    

# s = str(input())

# n,m = s.split()

# n = int(n)
# m = int(m)

n = int(input())
m = n

list = []

for i in range(0,n):
    new = []

    ip = str(input())

    a = ip.split()

    for z in range(0, len(a)):
        a[z] = int(a[z]) 
        new.append(a[z])

    list.append(new)    
        

k = int(input())

tongTren = 0
tongDuoi = 0

for i in range(0,n):
    for j in range(0,m):
        if(i>j):
            tongTren += list[i][j]
        if(i<j):
            tongDuoi += list[i][j]    


if(abs(tongTren-tongDuoi)<k):
    print("YES")   
else:
    print("NO")  

print(abs(tongDuoi-tongTren))           
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

tongAll = 0
tongTren = 0
p = int(n-1)

for i in range(0,n):
    list[i][p] = 0
    p-=1

# for i in range(0,n):
#     q = ""
#     for j in range(0,m):
#         q+=str(list[i][j])+" "

#     print(q)    

for i in range(0,n):
    for j in range(0,m):
        tongAll += list[i][j] 

for i in range(0,n):
    for j in range(0,m):
        if(list[i][j]==0):
            break  
        else:
            tongTren += list[i][j]      

tongDuoi = int(tongAll - tongTren)

# print(tongDuoi)
# print(tongTren)

if(abs(tongTren-tongDuoi)<=k):
    print("YES")   
else:
    print("NO")  

print(abs(tongDuoi-tongTren))      

      
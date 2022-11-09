def UCLN(a,b):
    if b == 0 :
        return a
    return UCLN(b,a % b)

s = str(input())

n, k = s.split()

n = int(n)
k = int(k)

max = int( pow(10,k) )
min = int( pow(10,k-1))

tong = 0

z = ""

for x in range(min, max):
    if(UCLN(x,n)==1):
        tong+=1
        z += str(x)+" "

    if(tong==10):
        print(z)
        z=""
        tong = 0    

print(z)
def ucln(a,b):
    if(a == 0 or b == 0): return a+b

    while a!=b:
        if(a > b): a-=b
        else: b-=a

    return a     

def snt(a):
    if(a<2): return 0

    sr = int(math.sqrt(a))

    for i in range(2, sr+1):
        if(a%i == 0): return 0

    return 1  




test = int ( input())

while test>0:
    test -= 1

    so1 = int( input() )

    so2 = ""

    so3 = so1

    z = 1

    while(so3 != 0):
        so2 += str(so3%10)
        so3 = so3//10

    so2 = int(so2)

    if(ucln( so2, so1 ) == 1): print("YES")
    else: print("NO")
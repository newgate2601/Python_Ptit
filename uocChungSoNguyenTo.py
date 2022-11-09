import math

def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

test = int(input())

while(test>0):
    test-=1

    s = str(input())

    n, m = s.split()

    n = int(n)
    m = int(m)


    z = math.gcd(n,m)

    s = str(z)

    kq = 0

    for x in s:
        kq += int(x)

    if(nto(kq)==True):print("YES")
    else:print("NO")    


def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)    

test = int(input())

while(test>0):
    test-=1

    n = int(input())
    m = int(input())

    print(uscln(n,m))
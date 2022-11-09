test = int( input() )

while(test > 0):
    test-=1

    n = int(input())

    tong = float(0)

    if(n%2==1):
        i = int(1)
        while(i <= n ):
            tong += 1/i
            i+=2
    else:
        i = int(2)
        while(i<=n):
            tong += 1/i
            i+=2

    print('%.6f' %tong)    
        




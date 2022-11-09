
test = int( input() )

while(test>0):
    test-=1

    tong = 0

    n = str( input() )

    for x in n:
        tong += int(x)


    so2 = ""

    so3 = tong

    z = 1

    while(so3 != 0):
        so2 += str(so3%10)
        so3 = so3//10

    so2 = int(so2)

    if( so2 < 10 ): print("NO")
    else:
        if(tong==so2):print("YES")
        else:print("NO")
        
    




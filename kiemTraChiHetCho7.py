test = int (input())

while(test>0):

    test-=1

    so1 = int( input() )

    check = 0

    i = 0
    while(i < 1000):

        if(so1 %7 == 0):
            print(so1)
            check = 1
            break

        else:
            so2 = ""

            so3 = so1

            z = 1

            while(so3 != 0):
                so2 += str(so3%10)
                so3 = so3//10

            so2 = int(so2)

            so1 = so1 + so2

    if(check == 0): print(-1)

    

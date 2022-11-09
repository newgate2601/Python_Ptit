import math


def snt(n):
    if(n<2):
        return 0

    can = int(math.sqrt(n)) 

    for i in range(2, can +1):
        if(n%i==0):
            return 0

    return 1   

test = int(input())

while(test>0):

    test-=1

    n = str(input())

    if(snt( int(n) ) != 1):
        print("No")
    else:
        
        n = str(n)
        s = n[::-1]

        if(snt( int(s) ) !=1 ):
            print("No")

        else:
            
            n = int(n)

            check = 1

            while(n>0):

                z = int(n%10)

                if(snt(z)!=1):
                    check = 0
                    break

                n = int(n/10)

            if(check==0):
                print("No")
            else:
                print("Yes")    
            
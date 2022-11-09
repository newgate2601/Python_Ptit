import math

def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True



test = int( input() )

while(test>0):
    test-=1

    s = str(input())

    if( nto(len(s)) == False ):
        print("NO")
    else:
        dem = 0
        check = 0

        for x in s:
            if( nto(int(x)) == True ):
                dem+=1   
            if( dem > len(s) - dem ):
                check = 1
                break

        if(check == 1):
            print("YES")
        else:
            print("NO")    
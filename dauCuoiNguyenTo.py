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

    if(len(s)<4):
        print("NO")
    else:
        dau = 100*int ( s[0] ) + 10*int ( s[1] ) +int ( s[2] ) 
        cuoi = int( s[len(s)-1] ) + 10*int( s[len(s)-2] ) + 100*int( s[len(s)-3] )

        if(nto(dau)==True and nto(cuoi)==True):
            print("YES")
        else:
            print("NO")    



    
        
    




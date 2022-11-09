import math

def nto(n) :
    if n < 2 : return False
    for i in range(2, int(math.sqrt(n)) + 1) :
        if n % i == 0 : return False
    return True

test = int(input())

while(test>0):
    test-=1

    n = int(input())

    z = n

    s = "1"

    for i in range(2, z+1):
        if(nto(n)==True):
            s += str(" * " +str(int(n))+"^1")
            n=1
        elif(n==1):    
            break
        else:
            if(nto(i)==1 and n%i ==0):
                dem = 0
                while(n%i==0):
                    dem+=1
                    n=n/i
                s += str(" * " + str(i)+"^"+str(dem))       

    print(s)
test = int( input())

while(test > 0):
    test-=1

    s = str(input())

    tong = 1

    arr = ""

    check = 1

    for i in range(0, len(s)-1):
        if( s[i] !=  s[i+1]):
            arr += str(tong)+s[i]
            check = 0
            tong = 1
        else:
            tong+=1

    arr+= str(tong) + s[len(s)-1]

    if(check==0):print(arr)    
    else:print( str(len(s))+s[0] )    
            


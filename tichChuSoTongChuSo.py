
test = int( input())

while( test > 0 ):
    test-=1

    s = str(input())

    checkTich = 0

    tich = 1

    tong = 0
    
    for i in range(0, len(s)):
        if(i%2==1):
            tong += int( s[i] )
        else:
            if( int(s[i])!=0 ):
                tich*= int(s[i])    
    
    k = "" + str(tich)+" "+str(tong)    

    print(k)    
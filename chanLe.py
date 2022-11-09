test = int( input() )

while test>0:
    test-=1
    tong = 0

    s = str( input() )
    
    for x in s:
        tong += int(x)

    if(tong % 10 != 0): print("NO")
    else:
        check = 1
        for i in range( len(s)-1 ):
            if( int(s[i]) - int(s[i+1]) != 2 and int(s[i+1]) - int(s[i]) !=2 ):
                check=0
                break

        if(check == 0):print("NO")
        else: print("YES")         

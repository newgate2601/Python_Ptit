test = int( input() )

while test > 0:
    test-=1

    s = str( input() )

    check = 1

    for x in range(len(s) - 1 ):
        if( int(s[x]) >  int(s[x+1]) ):
            check = 0
            break

    if(check == 1): print("YES")
    else: print("NO")    
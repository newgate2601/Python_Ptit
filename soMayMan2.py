test = int( input() )

while( test > 0 ):
    test -= 1

    s = str(input())

    check = 1

    for x in s:
        if(x!='4' and x!='7'):
            check = 0
            break

    if(check == 1):print("YES")
    else: print("NO")     

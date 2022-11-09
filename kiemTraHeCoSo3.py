test = int( input() )

while(test>0):
    test-=1

    s = str(input())

    check = 1

    for x in s:
        if(x != '0' and x != '1' and x != '2'):
            check = 0
            break

    if(check == 1):print("YES")
    else: print("NO")    
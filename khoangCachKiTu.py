import math

test = int(input())

while(test>0):
    test-=1

    s = str(input())

    dao = s[::-1]
    check = 1

    for i in range(1, len(s)):          
        if( abs( ord(s[i]) - ord(s[i-1]) ) != abs( ord(dao[i]) - ord(dao[i-1]) ) ):
            check = 0

    if(check == 1):print("YES")
    else:print("NO")        


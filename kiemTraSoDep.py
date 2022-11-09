

test = int(input())

while(test>0):
    test-=1

    s = str(input())

    if(s[0]==s[1]):print("NO")
    else:
        
        check = 1

        for i in range(0, len(s)):
            if(i%2==0):
                if(s[0]!=s[i]):
                    check = 0
            if(i%2==1):
                if(s[1]!=s[i]):
                    check = 0        

            if(check == 0):
                break

        if(check==1):print("YES")
        else:print("NO")

      


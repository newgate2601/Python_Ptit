test = int(input())

while(test>0):
    test-=1

    n = int(input())
    q = ""
    for i in range(22,n,2):
        
        s = str(i)
        sn = s[::-1]
        if(len(s)%2==0 and s==sn):
            check = 1

            for j in range(0,len(s)):
                if( int(s[j])%2==1 ):
                    check = 0
                    break

            if(check==1):
                q+=str(i)+" "


    print(q)
          
        

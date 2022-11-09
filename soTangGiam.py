test = int(input())

while(test>0):
    test-=1

    n = int(input())

    s = str(n)

    if(len(s)<3):
        print("NO")
    else:
        viTri = -1
        check = 1

        for i in range(0, len(s)-2):

            if( int( s[i] ) >= int(s[i+1]) ):
                viTri = i+1
                check = 0
                break

        if(check == 1):
                print("YES")
        else:
                check2 = 1
                for i in range(viTri,len(s)-1):
                    if(int(s[i]) <= int(s[i+1]) ):
                        print("NO")    
                        check2 = 0
                        break

                if(check2==1):
                    print("YES")    
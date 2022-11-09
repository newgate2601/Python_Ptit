test = int( input() )

while test>0:
    test-=1

    s = str ( input())

    tong = int(0)

    tong += int(s[ len(s)-1 ] )+ int(s[ len(s)-2 ])*10

    if(tong == 86): print("YES")
    else: print("NO")

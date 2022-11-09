test = int( input() )

while test>0:
    test-=1

    day = ""

    s = str(input())

    for i in range( len(s) - 1 ):
        if( s[i] >= 'A' and s[i] <= 'Z' ):
            k = int(s[i+1])
            while k>0:
                k-=1
                day += s[i]

    print(day)            


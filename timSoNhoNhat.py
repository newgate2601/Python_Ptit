test = int(input())

while(test>0):
    test-=1

    s = str(input())
    tong = 0
    for i in range(0, len(s) ):
        if(s[i]>='a' and s[i]<='z'):
            s  = s[0:i] +" "+ s[(i+1):]


    list = s.split()
    
    min = 999999999

    for i in range(0, len(list)):
        if( int(list[i]) < min ):
            min = int(list[i])

    print(min)
test = int(input())

while(test>0):
    test-=1

    n = int(input())

    list = [1]*n

    b = [0]*1002

    for i in range(0, n):
        list[i] = int(input())
        b[list[i]]+=1

    max = -1
    iMax = -1

    for i in range(0, n):
        if(b[list[i]]>max):
            max = b[list[i]]
            iMax = list[i]

        if(b[list[i]]==max and iMax > list[i] ):
            max = b[list[i]]
            iMax = list[i]    

    print(iMax)        
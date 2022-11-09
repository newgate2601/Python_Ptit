test = int(input())

while(test>0):
    test-=1

    n = int(input())

    check = int(n/2)

    s = str(input())

    list = s.split()
    b = [0] * 1000001

    for i in range(0, len(list)):
        list[i] = int(list[i])
        b[list[i]]+=1

    max = -1
    so = -1
    for i in range(0, len(list) ):
        if(b[list[i]]>max):
            max = b[list[i]]
            so = list[i]

    if(max > check):
        print(so)
    else:
        print("NO")                

    

      
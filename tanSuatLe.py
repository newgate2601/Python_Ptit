test = int(input())

while(test>0):
    test-=1
    n = int(input())

    s = str(input())

    list = s.split()

    b = [0] * 1000004

    for i in range(0, n):
        list[i] = int(list[i])
        b[list[i]] += 1

    max = -1
    vTri = -1

    for i in range(0,n):
        if(b[list[i]] % 2 == 1):
            max = b[list[i]]   
            vTri = list[i] 

    print(vTri)
test = int(input())

while(test>0):
    test-=1

    n = int(input())

    c = str(input())
    d = str(input())

    a = c.split()
    b = d.split()

    for i in range(0,n):
        a[i] = int(a[i])
        b[i] = int(b[i])

    for i in range(0, n-1):
        for j in  range(i+1, n):
            if(a[i]>a[j]):
                t = a[i]
                a[i] = a[j]
                a[j] = t    

    for i in range(0, n-1):
        for j in  range(i+1, n):
            if(b[i]>b[j]):
                t = b[i]
                b[i] = b[j]
                b[j] = t                

    for i in range(0, n):
        for j in range(0,n):

            if(a[i]<=b[j] and b[j] != -9999 ):
                b[j] = -9999     
                break

    check = 1

    for i in range(0,n):
        if(b[i]!=-9999):
            check = 0
                      
    if(check == 1):
        print("YES")
    else:
        print("NO")                      
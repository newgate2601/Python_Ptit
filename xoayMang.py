
test = int(input())

while(test>0):
    test-=1

    s1 = str(input())

    n, k = s1.split()

    n = int(n)
    k = int(k)

    s2 = str(input())

    list = s2.split()

    for i in range(0, len(list)):
        list[i] = int(list[i])

    day = ""

    for i in range(k, len(list)):
        day += str(list[i])+" "

    for i in range(0, k):
        day += str(list[i])+" " 

    print(day)       

    

                 
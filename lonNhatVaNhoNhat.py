
while(1):


    n = int(input())

    if(n == 0):
        break

    list = [1]*n

    for i in range(0,n):
        list[i] = int(input())

    max = list[0]
    min = list[0]

    for i in range(0,n):
        if(list[i] < min):
            min = list[i]
        if(list[i] > max):
            max = list[i]     

    s = ""
    s = str(min) + " " + str(max)

    if(max!=min):
        print(s)
    else:
        print("BANG NHAU")               
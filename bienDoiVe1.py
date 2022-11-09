n = 1

while(n!=0):
    n = int(input())

    if(n==0):
        break

    if(n==1):
        print("1")

    else:

        tong = 1

        while(n!=1):
            if(n%2==0):
                tong+=1
                n = int(n/2)
            else:
                tong+=1
                n = n*3 + 1


        print(tong)

test = int(input())

while(test>0):
    test-=1

    n = int(input())

    s = str(input())

    max = -99999
    min = 99999

    list = s.split()
    b = [0] * 1002
    for i in range(0, len(list)):
        list[i] = int( list[i] )
        b[ list[i] ]+=1
        if(max < list[i]):
            max = list[i]
        if(min > list[i]):
            min = list[i]    

    dem = 0

    for i in range(min, max+1):
        if(b[i]==0):
            dem += 1

    print(dem)        


    




    
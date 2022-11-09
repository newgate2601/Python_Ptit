n = int(input())

list = ["1"]*n

for i in range(0 , len(list) ):
    list[i] = str(input())

dem = 0

for i in range(0, len(list)-1):
    check = 1

    if(list[i]!="kaka"):
        dem += 1

        for j in range(i+1, len(list)):
            if( list[i] != "kaka" and list[j] != "kaka" and list[i] == list[j] ):
                list[j] = "kaka"    
                check = 0

        if(check == 0):
            list[i] = "kaka"


print(dem)        
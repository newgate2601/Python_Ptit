n = int(input())

s = str(input())

list = s.split()

tong = 0

for i in range(0, len(list)):
    list[i] = int(list[i])

for i in range(0, len(list)-1):
    for j in range(i+1, len(list)):
        if((i<j and list[i]>list[j]) or (i>j and list[i]<list[j]) ):
            tong+=1

print(tong)        
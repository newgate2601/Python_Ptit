n = int(input())

s = str(input())

list = s.split()

tong = 0

for i in range(0, len(list)-1):
    if(list[i]!=list[i+1]):
        tong+=1

print(tong)        
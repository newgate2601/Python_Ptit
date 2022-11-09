n = int(input())

s = str(input())

list = s.split()

b = [0]*1000001

for i in range(0, len(list)):
    list[i] = int( list[i] )
    b[list[i]]+=1

for i in range(1, 30001):
    if(b[i]==0):
        print(i)   
        break




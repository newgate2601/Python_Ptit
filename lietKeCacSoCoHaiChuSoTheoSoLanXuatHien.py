s = str(input())

if(len(s) % 2 == 1):
    s = s[0: (len(s)-1) ] 

s = int(s)

list = []

while(s>0):

    list.append( int(s%100) )
    s = int(s//100)

b = [0]*102

for i in range(0, len(list)):
    b[list[i]]+=1

q = ""
for i in range(len(list)-1, -1,-1):
    if(b[list[i]]!=0):
        q += str(list[i])+" "
        b[list[i]] = 0

print(q)        
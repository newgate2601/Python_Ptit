s = str(input())
k = int(input())
if(len(s) % 2 == 1):
    s = s[0: (len(s)-1) ] 

s = int(s)
list = []

while(s>0):

    list.append( int(s%100) )
    s = int(s//100)

b = [0]*102

list = sorted(list)

check = 0

for i in range(0, len(list)):
    b[list[i]]+=1
    if(b[list[i]]>=k):
        check = 1



if(check==0):
    print("NOT FOUND")
else:
    for i in range(0, len(list)):
        if(b[list[i]]!=0 and b[list[i]]>=k):
            q = ""
            q+= str(list[i])+" "+str(b[list[i]])
            b[list[i]] = 0
            print(q)    
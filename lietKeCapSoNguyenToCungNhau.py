def uscln(a, b):
    if (b == 0):
        return a
    return uscln(b, a % b)

n = int(input())

s = str(input())

a = s.split()

b = [0]*1000001

for i in range(0, len(a)):
    a[i] = int( a[i] )


for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        if(a[i]>a[j]):
            t = a[i]
            a[i] = a[j]
            a[j] = t

for i in range(0, len(a)-1):
    for j in range(i+1, len(a)):
        s = ""
        if(uscln(a[i],a[j])==1):
            s = str(a[i])+" "+str(a[j])
            print(s)







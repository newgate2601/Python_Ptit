def UCLN(a,b):
    if b == 0 :
        return a
    return UCLN(b,a % b)

s = str(input())

l, r = s.split()
l = int(l)
r = int(r)

for x in range(l, r-1):
    for y in range(x+1, r):
        if(UCLN(x,y)==1):
            for z in range(y+1, r+1):
                if(UCLN(x,z)==1 and UCLN(z,y)==1):
                    xau = "("+str(x)+", "+str(y)+", "+str(z)+")"
                    print(xau)


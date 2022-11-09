test = int(input())

while(test>0):
    test-=1

    s = str(input())

    tong = 0

    

    for i in range(0, len(s)):
        if(s[i]>='0' and s[i]<='9'):
            tong += int(s[i])

    q = s.replace("0","")
    q = q.replace("1","")
    q = q.replace("2","")
    q = q.replace("3","")
    q = q.replace("4","")
    q = q.replace("5","")
    q = q.replace("6","")
    q = q.replace("7","")
    q = q.replace("8","")
    q = q.replace("9","")

    d = ''.join(sorted(q))
    d+=str(tong)

    print(d)

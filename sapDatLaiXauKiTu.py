test = int(input())
t = 1
while(test>0):
    test-=1
    op = ""
    op = "Test " + str(t)+": "
    t+=1
    s1 = str(input())
    s2 = str(input())


    s1 = sorted(s1)
    s2 = sorted(s2)

    if(s1==s2):
        op += "YES"
    else:
        op += "NO"    

    print(op)    
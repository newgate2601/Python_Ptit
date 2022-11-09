test = int(input())

while(test>0):
    test-=1

    s = str(input())
    sXoa = str(input())

    lenS = len(s)

    q = s.replace(sXoa,"")

    lenQ = len(q)

    print(int( int(lenS-lenQ) / int(len(sXoa)) ))
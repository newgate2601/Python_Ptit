
list = [1]*95


for i in range(3, 95):
    list[i] = list[i-1] + list[i-2]

test = int(input())

while(test>0):
    test-=1

    s = str(input())

    n, m = s.split()

    n = int(n)
    m = int(m)

    day = ""

    for i in range(n, m+1):
        day += str(list[i])+" "

    print(day)    
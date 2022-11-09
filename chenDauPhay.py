s = str(input())

dao = s[::-1]

tong = 0

daomoi = ""

for x in dao:

    if(tong==3):
        tong = 0
        daomoi += ","

    daomoi+=x
    tong+=1

s = daomoi[::-1]

print(s)
n = int(input())

s = str(input())

list = s.split()

for i in range(0, len(list)):
    list[i] = float(list[i])

mx = max(list)
mn = min(list)

list.remove(mx)
list.remove(mn)

for i in range(0, n):
    if(mx in list):
        list.remove(mx)
    if(mn in list):
        list.remove(mn)

dem = 0

for i in range(0, len(list)):
    dem += list[i]

kq = float(dem/len(list))

print( '%0.2f' %kq )
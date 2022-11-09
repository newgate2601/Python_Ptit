from re import T
from tokenize import String


s = str(input())

t = 0

for x in range(0, len(s)): 
    if( s[x] == '4' or s[x] == '7' ): t+=1

if(t == 4 or t == 7): print("YES")
else: print("NO")
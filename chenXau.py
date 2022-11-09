s1 = str(input())
s2 = str(input())
i = int(input())

s1 = s1[0:(i-1)] + s2 + s1[(i-1):]

print(s1)
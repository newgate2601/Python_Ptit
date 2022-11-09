
s = str( input() )

tu = ""

dem = 0

for i in range( len(s) - 1 ):
    if( s[i] !=  " " ): 
        tu += s[i]

    if( s[i+1] == " " ): 
        dem = i+2
        print(tu)
        tu = ""

xau = ""

for i in range( dem, len(s) ):
    xau += s[i]

print(xau)
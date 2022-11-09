
s = str( input() )

tong = 0
tong2 = 0

for x in s:
    if( x >= 'a' and x <= 'z' ): tong += 1
    else: tong2 += 1

if( tong >= tong2 ): print( s.lower() )
else: print( s.upper() )
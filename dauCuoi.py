test = int( input() )

while test > 0:
    test-=1
    
    so = str( input() )
    dai = len(so)

    soDau = int(so[0])*10 + int( so[1] )
    soCuoi = int( so[dai-2] )*10 + int( so[dai-1] )

    if(soCuoi == soDau): print("YES")
    else: print("NO")



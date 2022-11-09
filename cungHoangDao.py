test = int(input())

while(test>0):
    test-=1

    s = str(input())

    ngay, thang = s.split()

    ngay = int(ngay)
    thang = int(thang)

    if(  ( ngay >= 21 and thang == 3 ) or (ngay <= 19 and thang == 4 ) ):
        print("Bach Duong")

    if(  ( ngay >= 20 and thang == 4 ) or (ngay <= 20 and thang == 5 ) ):
        print("Kim Nguu")    

    if(  ( ngay >= 21 and thang == 5 ) or (ngay <= 20 and thang == 6 ) ):
        print("Song Tu") 

    if(  ( ngay >= 21 and thang == 6 ) or (ngay <= 22 and thang == 7 ) ):
        print("Cu Giai")  

    if(  ( ngay >= 23 and thang == 7 ) or (ngay <= 22 and thang == 8 ) ):
        print("Su Tu")    

    if(  ( ngay >= 23 and thang == 8 ) or (ngay <= 22 and thang == 9 ) ):
        print("Xu Nu")    

    if(  ( ngay >= 23 and thang == 9 ) or (ngay <= 22 and thang == 10 ) ):
        print("Thien Binh")  

    if(  ( ngay >= 23 and thang == 10 ) or (ngay <= 22 and thang == 11 ) ):
        print("Thien Yet")  

    if(  ( ngay >= 23 and thang == 11 ) or (ngay <= 21 and thang == 12 ) ):
        print("Nhan Ma")    

    if(  ( ngay >= 22 and thang == 12 ) or (ngay <= 19 and thang == 1 ) ):
        print("Ma Ket")     

    if(  ( ngay >= 20 and thang == 1 ) or (ngay <= 18 and thang == 2 ) ):
        print("Bao Binh")     

    if(  ( ngay >= 19 and thang == 2 ) or (ngay <= 20 and thang == 3 ) ):
        print("Song Ngu")           
while True:

    mod=str(input('Mod secin Kript-Dekript K/D: '))

    if mod == 'K':

        soz=str(input('Kript etmek ucun soz daxil edin: '))

        for i in soz:

            print(bin(ord(i)),end='')


        print('\n')

    if mod == 'D':

        kod=str(input('Dekript etmek ucun kod daxil edin: '))

        kodList=list(kod)
        
        ords=[]

        chars=''

        saygac=0
        
        for i in kodList:

            saygac=saygac+1
                        
            if saygac % 9 == 0:

                chars=chars+i
                ords.append(chars)
                chars=''

            else:
                chars=chars+i

        reqemler=[]
        
        for i in ords:

            reqemler.append(int(i,2))


        for i in reqemler:

            print(chr(i),end='')


        print('\n')

            

                
            

        

        

            

                
        

        

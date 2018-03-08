d = open("prvaizmera.txt", "w")

with open("BK_KANCEVCI.txt", "r") as dat:
    for line in dat:
        besede = line.split()
        ime = list(besede[0])
        
        if len(besede) > 2:
            odcitek = list(besede[2])
            
        tocke = [] 
        
          
        for i in range(12, len(ime)):
            tocke.append(ime[i])
            x = ''.join(tocke)
            x = x.lstrip('0')
        if ime[12] != '.':
            d.write('')
            
            
            
            
            
            
d.close()
dat.close()

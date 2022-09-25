a = input()
for i in range(0,8):
    if a.find('c=') != -1 :
        a = a.replace('c='," ")
            
    elif a.find('c-') != -1 :
        a = a.replace('c-'," ")
               
    elif a.find('dz=') != -1 :
        a = a.replace('dz='," ")
        
    elif a.find('d-') != -1 :
        a = a.replace('d-'," ")
    
    elif a.find('lj') != -1 :
        a = a.replace('lj'," ")
    
    elif a.find('nj') != -1 :
        a = a.replace('nj'," ")
    
    elif a.find('s=') != -1 :
        a = a.replace('s='," ")
    
    elif a.find('z=') != -1 :
        a = a.replace('z='," ")
    
    
print(len(a))
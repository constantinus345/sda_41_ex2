#Fibonaci incepe cu 1,1 apoi fiecare el e suma celor 2 anterioare
#1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,1597,2584,4181,6765

def fibo_recursive(indice):
    if indice==0 or indice==1:
        return 1
    else:
        return fibo_recursive(indice-1) + fibo_recursive(indice-2)


#Alternativa fara recursie, doar loop

def fibonaci_clasic(indice):
    
    a = 1
    b = 1
    
    if indice< 0:
        print(f"Input {indice} incorect, negativ")
    elif indice==0 or indice==1:
        return 1
    else:
        for i in range(1,indice):
            rez = a + b
            b = a
            a = rez
        return rez
    
print(fibonaci_clasic(9))


            
            
    
        

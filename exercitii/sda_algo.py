from time import perf_counter

timp_start = perf_counter()

def factorial_recursive(n):
    print(n)
    if n==0 or n==1:
        return 1
        #pentru ca 0! si 1! sunt 1
    else:
        return n*factorial_recursive(n-1)
    #functia se apeleaza pe ea insasi

numar = 2000000
print(factorial_recursive(20))

print(f"(n={numar}) Took = {perf_counter()-timp_start} seconds")


#Alternativa fara recursie, doar loop
def factorial_simplu(n):

    rezultat = 1
    for i in range(1, n+1):
        rezultat *= i
        # echivalent cu : rezultat = rezultat * i
    
    return rezultat

numar = 5
print(f"Rezultatul lui {numar}! = {factorial_simplu(5)}")


import time

start_time = time.perf_counter()

#primele n patrate perfecte

def lista_patrate_perfecte(n):
    lista_primele_n = []
    for nr in range(1, n+1):
        lista_primele_n.append(nr**2)
    
    return lista_primele_n

print(lista_patrate_perfecte(20)[-3:])

print(f"Took = {time.perf_counter() - start_time} sec")
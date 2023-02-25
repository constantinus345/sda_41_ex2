# 4. Scrieti o functie care creaza o lista de dictionare 
# cu cheile "numar", "patrat", "cub" si valorile respective 
# pentru primele n numere naturale
# 4.1. Stocati aceste dictionare intr-un fisier json
# 4.2. si intr-un fisier csv
# 4.3. calculati cat timp a durat executia (hint: time.perf_counter() de ex)

def creaza_lista_nr_patrat_cub(numar):

    listx = []
    for nr in range(1, numar+1):
        dictx = {}
        dictx[f"nr. insusi"] = str(nr)
        dictx['patrat'] = nr**2
        dictx['cub'] = nr**3
        listx.append(dictx)
    
    return listx

import json
Folder = 'D:/Python_Code/sda_41_ex2'
with open(f'{Folder}/lista_nr_patrat_cub.json', 'w') as f:
    json.dump(creaza_lista_nr_patrat_cub(10), f)

import pandas
#pentru stocare in csv folosim pandas from_records
tabel_1 = creaza_lista_nr_patrat_cub(10)
tabel = pandas.DataFrame.from_records(tabel_1)
tabel.to_excel('tabel_10.xlsx')

# 5. Validati un email folosind regex string@string.string

import re
# [.-_])*[A-Za-z0-9]+
regex = re.compile(r'([A-Za-z0-9])+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')

def isValid(email):
    if re.fullmatch(regex, email):
      print("Valid email")
    else:
      print("Invalid email")
      
isValid('andrei@ion.ro')

# 6. scrieti o functie care returneaza tipul 
# de date al unui obiect. 
# Apelati aceasta functie intr-un alt fisier.

from func_type import get_type

print(get_type([1,2]))

# 7. Scrieti o functie care imparte doua numere. 
# Daca numitorul este 0, 
# atunci trebuie sa aruncati o exceptie cu textul "Aoleu".

def impartire(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        raise ZeroDivisionError("Aoleu")

rezultat = impartire(9,0)
print(rezultat)
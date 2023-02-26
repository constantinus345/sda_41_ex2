""" 
Data structures in python built-in
- List [1,2] - elemente ordonate, mutable
- Tuple (1,2) - immutable list
- Dictionary {key:value} - nu sunt ordonate, mutable
- Set {1,2} - nu sunt ordonate, mutable, elemente unice, 
putem adauga elemente la set
- Frozen set - nu putem adauga elemente la frozen set
- String- o insiruire de caractere, immutable
- int
- float - numere rationale, cu virgula
- bool - True/False
"""

#Ce inseamna immutable
lisx = [1,2,3]
tupx = (1,2,3)
lisx[1] = 5
print(lisx)


tupx[1] = 5 #nu merge, tuple nu-si poate schimba elementele
#metaforic - lista in cement
print(tupx)

listx = ['a','b','c','a','d', 'b']
setx = set(listx)
print(setx)
setx.add("s")
print(setx)

setx_frozen = frozenset(listx)
setx_frozen.add("s") #nu merge, frozen set nu-si poate schimba elementele
print(setx_frozen)

#Pentru alte structuri de date, putem folosi librarii speciale
#de exemplu libraria collections

from collections import OrderedDict

dictx = OrderedDict()
dictx["a"] = 1
dictx["b"] = 2
dictx["c"] = 3
print(dictx)


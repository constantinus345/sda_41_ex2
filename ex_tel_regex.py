nr_telefon = '40-43- .88'
# vaslidatre nr telefon
#1 mai mult de 8 cifre

import re
digits = re.findall(r'\d+', nr_telefon)
numar_tel_cifra = int(''.join(digits))
print(numar_tel_cifra)

if len(str(numar_tel_cifra)) >= 8:
    print('Numarul de telefon ESTE valid dupa conditia 1')
else:
    print('Numarul de telefon NU este valid dupa conditia 1')
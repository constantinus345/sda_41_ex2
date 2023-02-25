import configs
import os
import pytesseract
import cv2
#pip install pytesseract
#tesseract trebuie sa-l instalati pe windows
#si sa dati o cale executabila
#pip install opencv-python pentru cv2
#cv2 ne ajuta sa citim imaginea, pytesseract sa extragem textul
import pandas
#pip install pandas, pentru a procesa tabele

def extrage_text_din_imagine(fisier_imagine, folder = configs.Folder_images):
    imagine = cv2.imread(f'{configs.Folder_images}/{fisier_imagine}')
    config_tess = ('-l eng --oem 1 --psm 4')
    text = pytesseract.image_to_string(imagine, config=config_tess)
    return text

def extrage_randuri_din_text(text):
    randurile = [x for x in text.splitlines() if len(x)>4]
    return randurile

def extragere_timp_din_text(text):
    timp = text.split(' ')
    #print(timp)
    data = timp[-2]
    ora = timp[-1]
    return (data, ora)

# print(extragere_timp_din_text('ata /Timp 2023-02-25 10:28'))

#functie care extrage valuta, valoarea si textul produsului
def extrage_denumire_valoare_valuta(linia):
    #print(linia_1)
    linia_curenta_lista = linia.split(' ')
    #print(linia_1_lista)
    valuta = linia_curenta_lista[-1]
    valoarea = linia_curenta_lista[-2]
    denumirea = ' '.join(linia_curenta_lista[:-2])
    #print(denumirea)
    return {'denumirea':denumirea, 'valoarea':valoarea, 'valuta':valuta}

# linia_ultima = randurile[-1]
# print(linia_ultima)
# print(extrage_denumire_val_valuta(linia_ultima))
def lista_de_json_cu_produsele(folder=configs.Folder_images):
    lista_dictionare_cu_produse = []
    lista_imagini = os.listdir(folder)
    for inx, imagine in enumerate(lista_imagini):
        #print(lista_imagini)
        
        text = extrage_text_din_imagine(imagine)
        randurile = extrage_randuri_din_text(text)
        #print(f'pentru imaginea {imagine} avem urmatoarele valori:')
        #print(f"din randurile = {randurile}, type = {type(randurile)}")
        data_ora = extragere_timp_din_text(randurile[0])
        #print(f"data = {data_ora[0]}, ora = {data_ora[1]}")
        for linie in randurile[1:]:
            dic_valori = extrage_denumire_valoare_valuta(linie)
            dic_valori['data'] = data_ora[0]
            dic_valori['ora'] = data_ora[1]
            dic_valori['nume benzinarie'] = f"benzinarie_{inx+1}"
            #print(dic_valori)
            lista_dictionare_cu_produse.append(dic_valori)
        print(f"{'_'*50}")
    return lista_dictionare_cu_produse
    
    
lisx = lista_de_json_cu_produsele()
print(len(lisx))
print(lisx[0])
print(type(lisx[0]))
#pentru ca variabila din functie are un default, daca nu ii dam parametru, va lua valoarea default
#sau putem sa-i dam parametru, si sa ii dam alta valoare

# for imagine in lista_imagini:
#     print(f'pentru imaginea {imagine} avem urmatoarele valori:')
#     print(extrage_text_din_imagine(imagine))

# df = pd.DataFrame.from_records(data,index=['1', '2'])
# print(df)

tabel = pandas.DataFrame.from_records(lisx)
tabel.to_excel('tabel.xlsx')
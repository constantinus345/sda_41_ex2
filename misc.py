import pandas as pd

tabele = pd.read_html('https://bvb.ro/')

for tabel in tabele:
    print(len(tabel))
    print(tabel.columns)
    
print(tabele[0])
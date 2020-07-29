import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
import math
data = pd.read_excel (r'Öğrenciler - Bursa Uludağ Üniversitesi.xlsx',) 
df = pd.DataFrame(data, columns= ['Öğrenci No'])

# print(df)
result = []
x = float('nan')
for row in df.iterrows():
    if str(type(row[1][0])) == "<class 'str'>":
        # if not math.isnan(row[1][0]):

        result.append(row[1][0])
    elif str(type(row[1][0])) == "<class 'int'>":
        result.append(row[1][0])



# print(len(result))

# json_data = {'ctl00$cphC$txtIdentty':'12092196'}
# r = requests.get('https://yos.uludag.edu.tr/sonuc/', json=json_data)
# rep = requests.get('https://yos.uludag.edu.tr/sonuc/')

# f= open("mypost.html","w+")
# f.write(rep.text)

# print('oke')
# a = soup.select('label')
# print(a.find_next_sibling())

# for lab in soup.select("label"):
#     print(lab)
#     print(lab.find_next_sibling().text)

# print(soup)
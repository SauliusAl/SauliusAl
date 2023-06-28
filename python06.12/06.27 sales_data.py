import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data_sample.csv', encoding="ISO-8859-1")
# print(df.head(5))


# --------- 1 UZD: Suskirstykite klientus pagal šalį
"""1 VARIANTAS"""
# group_by_country = df.groupby('COUNTRY')
# print(group_by_country)
#
# plt.figure(figsize=(12, 6))
# group_by_country.size().plot(kind='bar')
#
# plt.title('salys pagal uzsakyma')
# plt.xlabel('salis')
# plt.ylabel('klientu kiekis')
# plt.show()

"""2 VARIANTAS, mazejancia tvarka, pirmas 10 saliu"""
# group_by_country = df['COUNTRY'].value_counts().nlargest(10)
#
# plt.bar(group_by_country.index, group_by_country.values)
# plt.title('salys pagal uzsakyma')
# plt.xlabel('Salis')
# plt.ylabel('Klientukieks')
# plt.xticks(rotation=90)
# plt.show()


# --------- 2 UZD: Atrinkite užsakymus, kurių suma viršija 5000 eurų

# df['TOTAL'] = df['QUANTITYORDERED'] * df['PRICEEACH']
# group_by_order = df[df['TOTAL'] > 5000][['CUSTOMERNAME', 'TOTAL']]
# df.to_csv('sales_data_sample.csv', index=False)
# print(group_by_order)

# --------- 3 UZD: Išfiltruokite užsakymus, kurie buvo pristatyti nuo 2003/9/30 iki 2005/03/15

# pirma keiciame datos formata, nes sistema nesupras musu parasytos datos formato
# df['ORDERDATE']=pd.to_datetime(df['ORDERDATE'], format='%d/%m/%Y %H:%M', errors='coerce')
# datu_filtravimas = df[(df['ORDERDATE'] >='9/9/2003') & (df['ORDERDATE']<='3/3/2005')]
# print(datu_filtravimas)

""" RUGILES VARIANTAS"""
# df["ORDERDATE"] = pd.to_datetime(df["ORDERDATE"])
# start_date = '2003-09-30'
# end_date = '2005-03-15'
# order_date = df[df['ORDERDATE'].between(start_date, end_date)]

# -------- 4 UZD: Išfiltruokite užsakymus, kurių statusas 'Disputed'

# disputed = df.[df['STATUS']=='DISPUTED




# -------- 5 UZD: Sukurkite skritulinę diagramą, kurioje būtų pavaizduota klientų skaičiaus pasiskirstymas pagal šalis


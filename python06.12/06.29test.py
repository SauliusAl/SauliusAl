
# ---- 1 UZDUOTIS:
# ------------- [+] Sukurkite klasę "Automobilis" su savybėmis "marke" ir "metai"
# ------------- [+] Sukurkite metodą "informacija", kuris išveda automobilio informaciją
# ------------- [+] Sukurkite vaikinę klasę "ElektrinisAutomobilis", kuri paveldi klasę "Automobilis" ir papildomai
# ------------------turi savybę "baterijos_talpa" ir metodą "baterijos talpa informacija", kuris išveda informaciją
# ------------------apie automobilio baterijos talpą


# class Automobilis:
#     def __init__(self, marke, metai):
#         self.marke = marke
#         self.metai = metai
#
# automobilis = Automobilis("Audi", 2020)
# print(f"Automobilis: ", '"Audi", 2020')
#
# class Elekrtomobilis:
#     def __init__(self, marke, metai, baterijos_talpa):           #sukuriame vaiko klase
#         self.marke = marke
#         self.metai = metai
#         self.baterijos_talpa = baterijos_talpa
#
# Elekrtomobilis = Elekrtomobilis("Audi", 2022, 60)
# print(f"Elektomobilis: ", '"Audi E-tron", 2022, 60')

# ---- 2 UZDUOTIS:
# ------------- [+] Naudodami pandas, nuskaitykite CSV failą "duomenys.csv" ir įrašykite duomenis
# ------------------į PostgreSQL duomenų bazės "students" lentelę
# ------------- [+] Pap. sąlyga: Įrašykite duomenis į "students" lentelę tik tuomet, jei amžius yra didesnis nei 20

# import pandas as pd
# import matplotlib.pyplot as plt
#
# df = pd.read_csv('duomenys.csv')
# print(df.head(5))



# ---- 3 UZDUOTIS:
# ------------- [+] Išskirkite produktų pavadinimus iš
# -----------------{https://www.rde.lt/categories/lt/1599/sort/5/filter/0_0_0_0/page/1/Dvira%C4%8Diai.html}
# ------------------puslapio naudodami Beautiful Soup ir išsaugokite juos į Pandas DataFrame stulpelį


import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import psycopg2


from db_config import create_table, insert_data, db_params

delay = 2
for i in range(1, 5):
    url = f'https://www.rde.lt/categories/lt/1599/sort/5/filter/0_0_0_0/page/{i}/Dvira%C4%8Diai.html'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')




# ---- 4 UZDUOTIS:
# ------------- [+] Išskirkite informaciją apie produktų kainas ir jų kategorijas iš pigu.lt puslapio naudodami
# -------------------Beautiful Soup ir išsaugokite juos į Pandas DataFrame
# ------------- [+]  Remdamiesi gautais duomenimis sukurkite stulpelinę diagramą, kurioje bus pavaizduotos
# -------------------produktų kainos pagal kategorijas mažėjančia tvarka

# import matplotlib.pyplot as plt
# import requests
# from bs4 import BeautifulSoup
# import pandas as pd
# import time
# import psycopg2
#
#
# from db_config import create_table, insert_data, db_params
#
# delay = 2
# for i in range(1, 5):
#     url = f'https://pigu.lt/lt/'
#     response = requests.get(url)
#     content = response.text
#     soup = BeautifulSoup(content, 'html.parser')


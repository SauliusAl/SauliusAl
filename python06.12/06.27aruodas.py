import matplotlib.pyplot as plt
import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import psycopg2


from db_config import create_table, insert_data, db_params, ikelti_duomenis

delay = 2
for i in range(1, 5):
    url = f'https://en.aruodas.lt/gyvenamieji-namai/puslapis/{i}/?FBuildingType=box'
    response = requests.get(url)
    content = response.text
    soup = BeautifulSoup(content, 'html.parser')

    skelbimai = soup.find_all('div', class_='list-row-v2 object-row selhouse advert')
    duomenys =[]
    """naudojamas unikalioms reiksmems"""
    unikalus = set()
    for skelbimas in skelbimai:
        kaina = skelbimas.find('span', class_='list-item-price-v2').text.strip()
        lokacija = skelbimas.select_one('.list-adress-v2 h3').text.strip()  #h3 teksto dydis, selektorius
        plotas = skelbimas.find('div', class_='list-AreaOverall-v2 list-detail-v2').text.strip()
        kaina = "".join(c for c in kaina if c.isdigit())

        unikalus_id = (kaina, lokacija, plotas)
        if unikalus_id not in unikalus:
            unikalus.add(unikalus_id)
            if ',' in lokacija:
                lokacija = lokacija.split(',')[0]       #split by first delimiter ','

            duomenys.append((kaina, lokacija, plotas))


    # df = pd.DataFrame(duomenys)
    # print(df)
    # df['kaina'] = pd.to_numeric(df['kaina'])


        # avg_price = df.agg({'Kaina': ['mean', 'min', 'max', 'size']})
    # print(avg_price)

    # avg_price_by_location = df.groupby('Lokacija')['kaina'].mean()
    # print(avg_price_by_location)

    #SKELBIMU PLOTO STATISTIKA

    # avg_square = df.agg({'Plotas': ['mean', 'min', 'max', 'size']})
    # print(avg_square)

    # create_table()
    # insert_data(duomenys)

data_from_db = ikelti_duomenis()
df = pd.DataFrame(data_from_db, columns=['kaina', 'lokacija', 'plotas'])
print(df)


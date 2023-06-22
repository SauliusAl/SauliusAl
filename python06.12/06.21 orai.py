# is www.meteo.lt/en/miestas?placeCode=Vilnius (06.21-06.27) isvesti koks buvo oru savaites vidurkis
import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# define website
url = "http://www.meteo.lt/en/miestas?placeCode=Vilnius"

# response from the website / pasiima visa INFO is URL
response = requests.get(url)

# create a bs4(beautifulsoup4) object (musu objektas) to parse (analizuoti) the HTML content /
# soup, kad galetume pasiimti produktu (siuo atveju oru) info
soup = BeautifulSoup(response.content, 'html.parser')

# find all weather information in the class content city
week_days = soup.find_all('span', class_='date')

# print(weather_info)

temperature = soup.find_all('span', class_='big up-from-zero')

# kodel rasome [::2], tai jei be sio uzrasymo, dienu yra 7, o temp net 14. taip mestu klaidas
night_temp = [temperature.get_text() for temperature in temperature[::2]]

week_day = [day.get_text() for day in week_days]

temp_values = night_temp

data = {'weekday': week_day, 'temperature': temp_values}

df=pd.DataFrame(data)

df_sorted=df.sort_values(by='temperature')

plt.bar(df_sorted['weekday'], df_sorted['temperature'])

plt.xlabel('savaites diena')
plt.ylabel('temperatura')
plt.title('Oru prognoze Vilniuje')
# plt.ylim(0, 25)
plt.show()

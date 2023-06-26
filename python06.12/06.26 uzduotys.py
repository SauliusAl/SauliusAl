# employees.csv
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('employees.csv')

# ----------- 1 UZD: Apskaičiuoti vidurkį, sumą, minimumą, maksimumą ir kitus statistinius rodiklius
# ------------------stulpeliuose arba grupėse naudojant mean(), sum(), min(), max() ir kitas funkcijas

# group_average = df.groupby('FIRST_NAME')['SALARY'].mean()
# print(group_average)

# group_min = df.groupby('FIRST_NAME')['SALARY'].min()
# print(group_min)

# group_max = df.groupby('FIRST_NAME')['SALARY'].max()
# print(group_max)

# group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()
# print(group_stats)


# ------------ 2 UZD: Grupuoti duomenis pagal tam tikrą stulpelį ir atlikti agregavimo operacijas,
# --------------------pvz., apskaičiuoti bendrą sumą ar vidurkį kiekvienai grupės naudojant groupby() funkciją

# group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean']})
# print(group_agg)



# ------------ 3 UZD:  Atlikti reikiamus duomenų valymo veiksmus, pvz., pašalinti dublikatus, užpildyti trūkstamas
# -------------------reikšmes arba pašalinti netinkamas reiksmes





# ------------4 UZD: Sukurti naujus stulpelius, atlikdami skaičiavimus ar manipuliacijas su esamais stulpeliais,
# -------------------pvz., pridėti, sudėti arba suskaidyti reikšmes

    # def __init__(self):
    #     self.column = []
    # def create_column(self, age):
    #     post = {
    #         "pavadinimas": age,
    #     }
    #
    #     self.posts.append(create_column())
    #     print("stulpelis sekmingai sukurtas")


# ---5 UZD. Redaguoti duomenų tipus, pvz., konvertuoti skaičių tipo stulpelius į datų tipo stulpelius arba atvirkščiai





# ---------------- 6 UZD: Atlikti duomenų filtravimą, rūšiavimą ir sujungimą pagal sąlygas arba stulpelius





# ----------------- 7 UZD: Vizualizuoti duomenis naudojant įvairias diagramas ir grafikus

# plt.title('suvestines statistika pagal vardus ir ju atlyginimus')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')


# plt.show()

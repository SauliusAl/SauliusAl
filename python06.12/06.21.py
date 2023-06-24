# import pandas as pd
# import matplotlib.pyplot as plt

# Dienmate duomenu struktura, kuri saugo vienos eilutes duomenis su indeksais
# data = pd.Series([10, 20, 30, 40, 50])
# print(data)


# Dvimate duomenu struktura, kuri saugo vienos eilutes duomenis lenteles pavidalu su stulpeliu ir eiluciu indeksais

# data = {'Name': ['Mantas', 'Deividas', 'Migle', 'Ausrine'],
#         'Age': [29, 27, 24, 45],
#         'City': ['Marijampole', 'Vilnius', 'Silute', 'Vilnius']
#         }



# df = pd.DataFrame(data)
# print(df)

# Atvaizduojame pirmas 4 eilutes DataFrame

"""skirtumas su (df) yra tas, kad (df) spausdina viska, o siuo atveju tai, ko reikia"""
# print(df.head(2))

# selected_columns = df[['Name', 'City']]
# print(selected_columns)

# prideti nauja stulpeli

# df['Salary'] = [1600, 1400, 1300, 1200]
# print(df)


# grupuokime duomenis pagal miesta ir gaukime vidutini altyginima

# average_salary_by_city = df.groupby('City')['Salary'].mean()
# print(average_salary_by_city)
# MEAN() naudojama apskaiciuoti vidurki
# average_age = df['Age'].mean()
# print(f"Average age: {average_age}")

# filtered_data = df[df['Age'] > 28]
# print(filtered_data)

# filtered_data = df[df['Age'] > 28][['Name', 'Age']]
# print(filtered_data)


# df = pd.read_csv('employees.csv')
# print(df.head(5))

# grupuoti pagal 'first_name' stulpeli ir suskaiciuoti jo dydi

# group_sizes = df.groupby('FIRST_NAME').size()
# print(group_sizes)

# suskaiciuosim vidurki atlyginimo
# group_average = df.groupby('FIRST_NAME')['SALARY'].mean()
# print(group_average)

# group_stats = df.groupby('FIRST_NAME')['SALARY'].describe()
# print(group_stats)

# group_max = df.groupby('FIRST_NAME')['SALARY'].max()
# print(group_max)

# group_agg = df.groupby('FIRST_NAME').agg({'SALARY': ['sum', 'mean', 'max']})
# print(group_agg)


# atvaizduojama linijine diagrama - group_agg.plot(kind='line') kaip linijine diagrama
# jei pakeistume į group_agg.plot(kind='pie', subplots=True, figsize=(8, 4)), atvaizduotu kitaip
# jei tai butu taip: group_agg.plot(kind='bar', figsize=(8, 4)), atvaizduotu barais
# group_agg.plot(kind='bar', figsize=(8, 4))
# pridedamos diagramos antrastes
# plt.title('suvestines statistika pagal vardus ir ju atlyginimus')
# plt.xlabel('Vardas')
# plt.ylabel('Atlyginimas')


# plt.show()


# atvaizduojama diagrama, kad tai veiktu, turi buti atkomentuota: 1, 2, 50, 55, 59, 62, 65, 68, 75, 77, 78, 79, 82
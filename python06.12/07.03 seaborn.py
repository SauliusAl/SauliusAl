import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error



# # pavyzdiniai duomenys
# data = sns.load_dataset('tips')

# stiliaus mustatymas
# sns.set_style('whitegrid')

# braizome stulpeline diagrama

# sns.barplot(x='species', y='sepal_length', data=data)
# sns.scotterplot(x='total_bill', y='tip', data=data)
# sns.lineplot(x='total_bill', y='tip', data=data)
# sns.histplot(x='total_bill', data=data)
# sns.boxplot(x='day', y='total_bill', data=data)

# numeric_cols = data.select_dtypes(include=['float64', 'int64']).columns
# koreliacija = data[numeric_cols].corr()
# sns.heatmap(koreliacija, annot=True, cmap='coolwarm')

# sns.violinplot(x='day', y='total_bill', data=data)
# sns.pairplot(data)

# diagramos pavadinimas
# plt.title('tips by total bill')
#
# plt.show()


# data = sns.load_dataset('diamonds')
# column_names = data.columns
# print(column_names)

# norime atvaizduoti karatus ir kaina
# sns.scatterplot(x='carat', y='price', data=data)
# plt.title('Distribution of price')
# plt.show()

# ---- objektas, grupuojame pagal deimantu apdirbima
# obj = sns.FacetGrid(data, col='cut')
# obj.map(sns.histplot, 'carat')
# plt.show()

# ----oblektas, grupuojame pagal spalvos derinima (deimantams), vid.price reiksmiu stulpeliai
# sns.barplot(x='cut', y='price', hue='color', errorbar=None, data=data)
# plt.show()

# obj = sns.FacetGrid(data, hue='color', col='cut')
# obj.map(sns.barplot, 'carat', 'price')
# plt.show()

# isanalizuoti kaip keiciasi isgyvenusiuju skaicius pagal keliones klase


# --- Titanic duomenys - kiek daug isgyveno pagal bilietu klases
# data = sns.load_dataset('titanic')
# survived_counts = data['pclass'][data['survived']==1].value_counts().sort_index()
# print(data)
# sns.barplot(x=survived_counts.index, y=survived_counts.values)
# --- metodas, padedantis pavaizduoti skaitine reiksme stulpeliuose
# for i, count in enumerate(survived_counts.values):
#     plt.text(i, count, str(count), ha='center', va='bottom')
# total_survived = data['survived'].sum()
# plt.xlabel('Keliones klase')
# plt.ylabel('Isgyvenusiuju skaicius pagal klase')
# plt.title('Isgyvenusiuju pagal keliones klase diagrama')

# plt.show()

# ------- STATISTINIAI MODELIAI 20:45 -------------------------

# iris = load_iris()
# X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2, random_state=42)
# knn = KNeighborsClassifier(n_neighbors=3)

# ---- treniruojamas klasifikatorius
# knn.fit(X_train, y_train)
# ---- prognozuojami rezultatai

# y_pred = knn.predict(X_test)


# --- Ivertinamas tikslumas
# accuracy = accuracy_score(y_test, y_pred)
# print('Tikslumas: ', accuracy)

# ------------------------
#  sugeneruojami duomenys
# x,y = make_blobs(n_samples=100, n_features=2, centers=3, random_state=42)

# inicializuojamas klasterizavimo modelis (musu atveju K-means)

# kmeans = KMeans(n_clusters=3, n_init='auto')

# priskiriame duomenis klasteriams

# labels = kmeans.fit_predict(x)

# ivertiname klasterizavimo rezultatus

# silhouette = silhouette_score(x, labels)
# print(silhouette)


# ------------ TIESINE REGRESIJA
# data = {
#     'X': [1, 2, 3, 4, 5],
#     'Y': [2, 4, 5, 4, 5]
# }
#
# df = pd.DataFrame(data)
# X = df[['X']]
# y = df['Y']

#  inicializuojama linijines regresijos modelis
# model = LinearRegression()
# model.fit(X, y)
# y_pred = model.predict(X)
# print('Nuokrypis:', model.intercept_)
# print('Koeficientas: ', model.coef_)
# sns.regplot(x='X', y='Y', data=df)
# plt.show()

# ---------------------
# data = sns.load_dataset('diamonds')
# X = data[['carat', 'depth', 'table']]
# y = data['price']

# X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)
# model = LinearRegression()
# model.fit(X_train, y_train)

# y_pred = model.predict(X_test)
# # ivertiname modelio tiksluma naudojant vidutini kvadratini nuokripi
# mse = mean_squared_error(y_test, y_pred)
# print('Vidutinis kvadratinis nuokrypis (MSE): ', mse)
# atvaizduojame prognozes ir tikras reiksmes naudojant regresijos diagrama
# df = pd.DataFrame({'Predicted price': y_pred, 'Actual price': y_test})
# sns.regplot(x='Actual price', y='Predicted price', data=df)
# plt.show()
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# sukuriame np array (Masyvas)

# arr = np.array([1, 2, 3])
# arr2 = np.array([4, 5, 6])
# result = arr + arr2
# print(result)


# arr = np.array([1, 2, 3, 4, 5])
# result = np.square(arr) # KELIMAS KVADRATU
# value = arr[1]  # indeksavimas
# print(value)

# array slicing
# sliced_arr = arr[-3:]
# print(sliced_arr)

#---------------- dauginama matrica is matricos
# matrica = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# matrica2 = np.array([[10, 11, 12], [13, 14, 15], [16, 17,18]])
#
# daugyba = np.dot(matrica, matrica2)
# print(daugyba)
#--
# daugyba [0, 0] = (1*10) + (2*13) + (3*16) = 84
#-----------
# random_numbers = np.random.randint(0,10, size=5)
# print(random_numbers)
#-------------------
# numbers = np.linspace(0,1,5)
# print(numbers)
#------------------ sugeneruoja skaiciu seka
# sequence = np.arange(10)
# print(sequence)

#----------------------- importuojames matplotlib.pyplot as plt, , spausdinama SINUSOIDE su 100 tasku
# x = np.linspace(0,10,100)
# y = np.sin(x)
#
#
# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Sinusine funkcija')
# plt.show()
#--------------- taskiukai, siaip atsitiktinai
# x = np.random.rand(10)
# y = np.random.rand(10)
#
# plt.scatter(x,y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Random points')
# plt.show()
#----------------------- sugeneruojami atsitiktiniai skaiciai ir rodo sk kieki kiekvienoje dimensijoje
# data = np.random.randn(1000)
#
# plt.hist(data, bins=20) # bins=20 reiskia, kiek yra stulpeliuku
# plt.xlabel('Values')
# plt.ylabel('Frequency')
# plt.title('Histogram')
# plt.show()

#-------------------- salygu taikymas
# masyvas = np.array([1, 2, 3, 4, 5])
#
# daugiau_uz_du = masyvas[masyvas > 2]
# print(daugiau_uz_du)

#-----jei vietoj masyvo butu array...
# masyvas = np.array([1, 2, 3, 4, 5])
#
# daugiau_uz_du = np.where(masyvas > 2)
# print(daugiau_uz_du)

#-----------
# arr1 = np.array([True, False, True])
# arr2 = np.array([False, True, True])
# result = np.logical_and(arr1, arr2)
# print(result)

#------------ isskiria masyva ties nurodytais skaitmenimis, skeliama i 2 dalis po 3 skaicius
# arr = np.array([1,2,3,4,5,6])
# change_arr = np.reshape(arr, (2,3))
# print(change_arr)

#------ array dalina i 3 dalis
# arr = np.array([1,2,3,4,5,6])
# splitting = np.split(arr, 3)
# print(splitting)

#------- surusiuoja eiles tvarka
# arr = np.array([4, 3, 2, 1, 6, 5])
# sorting = np.sort(arr)
# print(sorting)

#-------- grazina tik unikalias, nepasikartojancias reiksmes
# arr = np.array([4, 3, 2, 1, 6, 5, 4, 2, 1, 5, 10, 15])
# unique = np.unique(arr)
# print(unique)

#--------- UZDAVINYS, SU AKCIJOMIS
# vienos imones akciju kaina skirtingomis dienomis
akcijos = np.array([100, 110, 120, 115, 105, 95, 105, 100])

# apskaiciuojame dienos pelna ir nuostoli
dienos_pelnas = akcijos[1:] - akcijos[:-1]
dienos_nuostolis = akcijos[:-1] - akcijos[1:]

# randame diena su didziausia ir maziausia akciju kaina
didziausia_reiksme = np.max(akcijos)
didziausios_reiksmes_indeksas = np.argmax(akcijos)
maziausia_reiksme = np.min(akcijos)
maziausios_reiksmes_indeksas = np.argmin(akcijos)

# apskaiciuojame akciju kainos svyravimus
kainos_svyravimas = np.ptp(akcijos) # ptp skaiciuoja skirtuma tarp didziausios ir maziausios reiksmes

print(f'Dienos pelnas: {dienos_pelnas}')
print(f'Dienos nuostolis: {dienos_nuostolis}')
print(f'Didziausia akciju kaina: {didziausia_reiksme}, diena: {didziausios_reiksmes_indeksas +1}')
print(f'Maziausia akciju kaina: {maziausia_reiksme}, diena: {maziausios_reiksmes_indeksas +1}')

print(f'Akciju kainos svyravimas: {kainos_svyravimas}')

#--- sukurti linijine diagrama pagal aksiju kaina

x = np.array([1, 2, 3, 4, 5, 6, 7, 8])
y = akcijos

plt.plot(x, y)
plt.xlabel('Diena')
plt.ylabel('Kaina')
plt.title('Akciju kainos')
plt.show()





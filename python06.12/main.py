
# """
# Multi-komentavimas
# """

# vardas = "Saulius"
# amzius = 50
# print(vardas)
# print(amzius)


# vardas = "Saulius"
# amzius = 50
# arVartotojasAktyvus = Fals
# print(type(vardas))
# print(amzius)
# produktoKaina = 3.99

zodis = "Kaunas"

miestai = ["Vilnius", "Kaunas", "Klaipeda"]
# skaiciuSarasas = [1, 3, 53, 123, 1245, 12312]

# skaicius = int(input("Iveskite skaiciu: "))

# if skaicius > 0:
#     print("Skaicius yra teigiamas")
# elif skaicius < 0:
#     print("Skaicius yra neigiamas")
# else:
#     print("Skaicius yra nulis")

# """
# ---------------PRISKYRIMO OPERATORIAI
# = Priskyrimas
# += Prideda ir priskiria
# -= Atima ir priskiria
# *=
# /=
# %=
#
#
# -------------MATEMATINIAI OPERATORIAI
# +
# -
# *
# /
# %
# ** kelimas laipsniu
# // sveikoji dalyga
#
# Palyginimo operatoriai
# == lygu
# != nelygu
# >
# <
# >=
# <=
#
# LOGINIAI OPERATORIAI
# and
# on
# not
#
# NARYSTES OPERATORIAI
# in - kuris priklauso
# not in - kuris nepriklauso
#
# TAPATUMO OPERATORIAI
# is - YRA
# is not - NERA
# """

# if zodis in miestai:
#     print("Zodis " + zodis + " egzistuoja sarase")
#
# else:
#     print("Zodis nerastas")


# if len(skaiciuSarasas) > 0:
#
# print(len(miestai))
#
# if len(skaiciuSarasas) > 0:
#     print("Skaiciu sarasas pilnas")
# else:
#     print("Skaiciu sarasas tuscias")

# print("Mano vardas " + vardas + " As gyvenu " + miestai[0] + " mano amzius " + str(amzius))


# print(miestai[-2])

# miestai[1] = "Siauliai"
# miestai.append("Panevezys")
# miestai.insert(1, "Anyksciai")
# miestai,pop()
# del miestai[2]
# print(miestai)

# if amzius == 18:
#     print("Pilnametis")
#
# elif amzius == 24:
#     print("Daugiau nei 18")
# else:
#     print("Nepilnametis")


# skaicius = -1
#
# if skaicius >=0:
#     print("Skaicius yra teigiamas arba nulis")
# else:
#     print("Skaicius yra neigiamas")

# --------- 1 UZDUOTIS - Patikrinkite, ar studentas išlaikė egzaminą;
# ivertinimas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# islaikymoRiba = 5
# ivertinimas = int(input("Iveskite egzamino bala: "))
# if ivertinimas >= 5:
#     print("Egzaminas islaikytas")
# else:
#     print("Egzaminas neislaikytas")

# ------------ 2 UZDUOTIS - Patikrinkite, ar skaičius yra lyginis (PASITIKRINTI)
# Skaiciai = 5
# if Skaiciai % 2 == 0:
#     print("Lyginis skaicius")
# else:
#     print("Nelyginis skaicius")

#---- KITU VARIANTU NEBEVEIKIA
# sarasas = []
# ivertinimas = int(input("Iveskite skaiciu: "))
# if sarasas % 2 == 0:
#     print("lyginis skaicius")
#
# else:
#     print("nelyginis skaicius")

# --------- 3 UZDUOTIS - Patikrinkite, ar sąraše yra bent du skaičiai;
# sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if len(sarasas) >= 2:
#     print("yra 2 skaiciai")
# else:
#     print("nera 2 skaiciu")


# for i in range(1, 11):
#     print(i)
# -------------------------------------------------------
# vardai = ["Jonas", "Saulius", "Lina", "Marius", "Rugile"]

#     key     volue (paaiskinimas, kas cia per reiksmes)
# for vardas in vardai:
#     print(vardas)

# ---------------------- UZDUOTIS: ATRINTI IS SARASO SKAICIUS, KURIE YRA > 25
# skaiciai = [10, 20, 30, 40, 50, 23]
# atrinkti = []
# for skaicius in skaiciai:
#     if skaicius > 25:
#         atrinkti.append(skaicius)
# print("Atrinkti skaiciai: ", atrinkti)

# ----------------------- UZDUOTIS: ATRINKTI UNIKALIUS SKAICIUS IS SARASO
# skaiciai = [10, 10, 20, 44, 50, 50, 23, 23, 2, 45, 44, 11, 21]
#
# unikalios_reiksmes = []
#
# for skaicius in skaiciai:
#     if skaicius not in unikalios_reiksmes:
#         unikalios_reiksmes.append(skaicius)
#
# print("Unikalios_reiksmes: ", unikalios_reiksmes)

# ---------------------------------------------------
# -------------------------- FUNKCIJOS--------------
# def suma(a, b):
#     return a + b
#
# rezultatas = suma(2, 5)
#
# print("Suma: ", rezultatas)

# ------------
# def pasisveikinimas(vardas="Anonimas"):
#     print("Labas, ", vardas)
#
# pasisveikinimas("Saulius")

# ---------------- SUJUNGIA SARASUS
# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
#
# rezultatas = sujungti_sarasus([1, 2, 3], [4, 5, 6])
# print("Sujungtas sarasas: ", rezultatas)

# ------- ARBA KITAIP
# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas
#
# sarasas1 = [1, 2, 3]
# sarasas2 = [4, 5, 6]
# rezultatas = sujungti_sarasus(sarasas1, sarasas2)
# print("Sujungtas sarasas: ", rezultatas)

# --------------------------------------------
# ------------4 UZDUOTIS: Parašykite funkciją ar_lyginis, kuri priima vieną skaičių kaip argumentą ir patikrina,
#                        ar skaičius yra lyginis.
#                        Jei skaičius yra lyginis, tada funkcija turi grąžinti True, o jei nelyginis - False
# def ar_lyginis(skaicius):
#
#     if skaicius % 2 == 0:
#         return True
#     else:
#         return False
# print(ar_lyginis(6))

# ---------------------------------------------
# ------------5 UZDUOTIS: Parašykite funkciją didziausias_skaicius, kuri priima sąrašą skaičių ir
#                         grąžina didžiausią skaičių iš sąrašo
# def didziausias_skaicius(sarasas):
#     didziausias = sarasas [0]
# # ------------------(KUR CIA "0" REISKIA PIRMA IS SARASO SKAICIU)
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#     return didziausias
# skaiciusarasas = [2, 4, 5, 8, 16, 1, 18, 46, 24, 37]
# rezultatas = didziausias_skaicius(skaiciusarasas)
# print(rezultatas)

# --------------------------------------------
# ------------6 UZDUOTIS: Parašykite funkciją unikalios_reiksmes, kuri priima sąrašą ir grąžina
# ------------------------naują sąrašą, kuriame yra tik unikalios reikšmės iš pradinio sąrašo

# def unikalios_reiksmes(sarasas):
#     tuscias_sarasas = []
#     for reiksme in sarasas:
#         if reiksme not in tuscias_sarasas:
#             tuscias_sarasas.append(reiksme)
#
#         return tuscias_sarasas
# naujas_sarasas = [1, 3, 46, 78, 98, 16, 34, 17, 46, 16, 3]
# print(unikalios_reiksmes(naujas_sarasas))


# ------------ND 1 UZDAVINYS: Apskaičiuokite skaičių sąrašo suma, išskyrus tuos skaičius, kurie yra lyginiai.
# -----------------Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina sumą;
# def suma_nelyginiu(sarasas):
#     suma = 0
#     for nelyginis_skaicius in pradinis_sarasas:
#         if nelyginis_skaicius in sarasas:
#             if nelyginis_skaicius % 2 != 0:
#                 suma += nelyginis_skaicius
#     return suma
# pradinis_sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rezultatas = suma_nelyginiu(pradinis_sarasas)
# print(rezultatas)

# ---------------------viskas tas pats, tik su lyginiais

# def suma_lyginiu(sarasas):
#     suma = 0
#     for lyginis_skaicius in pradinis_sarasas:
#         if lyginis_skaicius in sarasas:
#             if lyginis_skaicius % 2 == 0:
#                 suma += lyginis_skaicius
#     return suma
# pradinis_sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# rezultatas = suma_lyginiu(pradinis_sarasas)
# print(rezultatas)



# ------------ND 2 UZDAVINYS: Raskite didžiausią skaičių iš Jūsų sukurto skaičių sąrašo.
# ------------Parašykite funkciją, kuri priima skaičių sąrašą kaip argumentą ir grąžina didžiausią skaičių
# NEVEIKIA
# pradinis_sarasas = [5, 9, 22, 38, 70, 10, 40, 77]
# def didziausias_skaicius(sarasas):
#     didziausias = sarasas [0]
#     for skaicius in sarasas:
#         if skaicius > didziausias:
#             didziausias = skaicius
#         return didziausias
# rezultatas = didziausias_skaicius(pradinis_sarasas)
# print(rezultatas)

# ------------ND 3 UZDAVINYS: Parašykite funkciją, kuri priima skaičių ir patikrina, ar jis yra pirminis skaičius
#
# def pirminis_skaicius (skaicius):
#     if skaicius < 2:
#         return False
#     for daliklis in range (2, skaicius):
#         if skaicius % daliklis == 0:
#             return False
#     return True
# skaicius = 10
# if pirminis_skaicius(skaicius):
#     print(f"skaicius {skaicius} yra pirminis skaicius")
# else:
#     print(f"skaicius {skaicius} yra ne pirminis skaicius")

#------------------------------------------------------------------------------
# def sujungti_sarasus(sarasas1, sarasas2):
#     sujungtas_sarasas = sarasas1 + sarasas2
#     return sujungtas_sarasas

# sarasas1 = [1, 2, 3]
# sarasas2 = [4, 5, 6]
# rezultatas = sujungti_sarasus(sarasas1, sarasas2)
# print("Sujungtas sarasas: ", rezultatas)
#
# if __name__ == '__mani__':
#     sujungti_sarasus(sarasas1, sarasas2)

